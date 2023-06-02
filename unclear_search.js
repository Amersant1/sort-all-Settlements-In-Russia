function clearAddr($addr) {
	
	$associate = array(
	" " => "", // Заодно и пробелы
	"д." => "",
	"стр." => "",
	"корп." => "",
	"ул." => "",
	"ул." => "",
	"пр." => "",
	"ш." => "",
	"г." => "",
	"пр-т." => "",
	"пр-т" => "",
	"пр-д." => "",
	"пр-д" => "",
	"пл-д." => "",
	"пл-д" => "",
	"пер." => "",
	"пер" => "",
	"микр.р-н" => "",
	"мкрн." => "",
	"мкрн" => "",
	"мкр." => "",
	"пл." => "",
	"пос." => "",
	"ст." => "",
	"с." => "",
	"б-р." => "",
	"б-р" => "",
	"пер-к" => "",
	"пер-к." => "",
	"1-й" => "",
	"2-й" => "",
	"3-й" => "",
	"4-й" => "",
	"5-й" => "",
	"6-й" => "",
	"7-й" => "",
	"8-й" => "",
	"9-й" => "",
	"1-я" => "",
	"2-я" => "",
	"3-я" => "",
	"4-я" => "",
	"5-я" => "",
	"6-я" => "",
	"7-я" => "",
	"8-я" => "",
	"9-я" => ""
	);

	$clrd_addr = strtolower(strtr($addr, $associate));
	
return $clrd_addr;
}

function getNums($search) {
	preg_match_all("/[0-9]*/", $search, $matches);
	$matches = array_diff($matches[0], array("")); // Удаляем пустые значения из $matches
return $matches;
}

function getMatchAdress($addr_string, &$Addr_array) {

	if(!isset($addr_string) || strlen($addr_string) < 1) return false;

	$list = array();
	$nums = getNums($addr_string); // Узнаем какие номера использованы в адресе
	$addr_string = clearAddr(preg_replace("/[0-9]*/", "", $addr_string)); // Удаляем сокращения и номера
	$word_parts = explode("\n", chunk_split(trim($addr_string), 2)); // Получаем массив с разбитым адресом по 2 символа
	array_pop($word_parts);

	// Пробегаем список имеющихся адресов
	foreach($Addr_array as $row) {
	
		$word_match = 0;
		$last_pos = 0;
		
		// Чистим попавшийся адрес
		$clr_row = clearAddr($row);
		$row_nums = getNums($row);
		
		// Пробегаемся по т.н. слогам входного адреса
		foreach($word_parts as $syllable) {
		
			$match_in = strpos($clr_row, strtolower(trim($syllable)), $last_pos); // Ищем слева-направо совпавший слог
			
			// Ловим совпадение слога с поправкой на ошибку
			if($match_in > -1 && $match_in < $last_pos + 4) {
				$last_pos = $match_in + strlen(trim($syllable));
				$word_match++;
			}
		
		}
		
		$all_percents = count($word_parts); // Количество частей в исходном слове
		$found_percents = $word_match; // Найдено совпадений подряд
		$match_perc = round($found_percents * 100 / $all_percents); // Считаем совпавший процент
		$max_point = 70; // Устанавливаем порог совпадения
		
		// Сверяем результаты и заполняем список для вывода результатов
		if($match_perc >= $max_point) {
		
			if(!empty($nums)) { // Если в адресе были номера
			
				foreach($nums as $num) {
					if(in_array($num, $row_nums)) $list[] = $row;
				}
			}
			else { // Если номеров небыло
				$list[] = $row;
			}
		}

	}

return $list;
}