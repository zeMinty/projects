//вычислятор дней в месяце
Date.prototype.our_daysInMonth = function (monthShift = 0) {
	let date = new Date(this.getFullYear(), this.getMonth() + monthShift, 32);
	return 32 - date.getDate();
};

//инсертер подстроки
function insertSubstr(str, pos, subStr) {
	str = str.toString();
	const result = str.slice(0, pos) + subStr + str.slice(pos);
	return result;
}

//реверсер строки
function reverseStr(str) {
	str = str.toString();
	return str.split("").reverse().join("");
}

//интизатор строки (соберет все цифры + минус если он в позиции 0)
function toInt(str) {
	let num = str.toString().replace(/((?!^)-+|[^\d\-]+)/gmi, '');
	if (num == '-') return 0;
	return num * 1;
}

//флотизатор строки (соберет все цифры, первый минус, первую запятую или точку)
function toFloat(str) {
	let num = str.toString().replace(/[^\d-.,]/, '').replace(',', '.'),
		dot = num.indexOf('.');
	dot = dot < 0 ? num.length : dot;
	let fi = num.substr(0, dot),
		se = num.substr(dot);

	fi = fi.replace(/(?!^)[^\d]+/gmi, '') * 1.0;
	se = se.replace(/[^\d]+/gmi, '') * 1.0;
	num = fi + '.' + se;

	if (num.replace(/[^\d]+/gmi, '') == '') return 0.0;
	return num * 1.0;
}

//монетизатор строки
function toMoney(number, post = '', pref = '') {
	number = toFloat(number);
	const flNumber = number.toFixed(2);
	let firstPart = '0',
		secondPart = '0',
		t = '';

	firstPart = reverseStr(flNumber.slice(0, flNumber.indexOf('.')));
	secondPart = flNumber.slice(flNumber.indexOf('.') + 1);

	for (let i = 0; i < firstPart.length; i += 3) t += firstPart.slice(i, i + 3) + ' ';
	firstPart = reverseStr(t);

	const result = firstPart.replace(/\- */, '-') + '.' + secondPart;

	return pref + result + post;
}

//проверяет пересечение элементов
function checkIntersect(e, c, strict = false) {
	var eR = e.getBoundingClientRect(),
		cR = c.getBoundingClientRect(),
		res = (
			(cR.top < eR.bottom)
			&& (cR.bottom > eR.top)
			&& (cR.right > eR.left)
			&& (cR.left < eR.right)
		) ? true : false;
	if (strict)
		res = (
			(cR.top <= eR.bottom)
			&& (cR.bottom >= eR.top)
			&& (cR.right >= eR.left)
			&& (cR.left <= eR.right)
		) ? true : false;
	return res;
}

//добавляет дни к переданой строке с датой в ISO формате
function addStringDay(strDate, daysQnt = 1) {
	if (strDate.match(/^\d{4}.\d{2}.\d{2}$/)) strDate += ' 00:00:00';
	if (!strDate.match(/^\d{4}.\d{2}.\d{2} \d{2}.\d{2}.\d{2}$/)) return false;

	const currentDate = new Date(strDate.replace(/(\d{4}).(\d{2}).(\d{2})[^\d]+(\d{2}).(\d{2}).(\d{2}).*/, '$1-$2-$3T$4:$5:$6.000Z')),
		oneDay = 1000 * 60 * 60 * 24;

	let nextDate = new Date(currentDate.getTime() + oneDay * daysQnt),
		strNextDate = nextDate.toISOString();

	strNextDate = strNextDate.replace(/(\d{4}).(\d{2}).(\d{2})[^\d]+(\d{2}).(\d{2}).(\d{2}).*/, '$1-$2-$3 $4:$5:$6');

	return strNextDate;
}

//цифрово-строковая сортировка
function numStrSort(arr, varl) {
	Array.prototype.sort.call(arr, ((a, b) => {
		let swap = 0,
			num1 = toInt(a[varl]),
			num2 = toInt(b[varl]);

		if (num1 && num2) { //сортировка по цифрам
			if (num1 > num2) swap = 1;
			if (num1 < num2) swap = -1;
			if (num1 == num2) swap = 0;
		}
		else {
			if (!num1 && !num2) { //сортировка по названиям
				if (a[varl] > b[varl]) swap = 1;
				if (a[varl] < b[varl]) swap = -1;
				if (a[varl] == b[varl]) swap = 0;
			}
			else if (!num1) swap = 1; //скидывание безцифорных вниз
			else if (!num2) swap = -1;
		}
		return swap;
	}));
}

//разница между датами
function diffDays(start, end) {
	const date1 = new Date(start),
		date2 = new Date(end),
		oneDay = 1000 * 60 * 60 * 24;

	let diffInTime = date2.getTime() - date1.getTime(),
		diffInDays = Math.round(diffInTime / oneDay);

	return diffInDays;
}