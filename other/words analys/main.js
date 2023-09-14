function numRound(num, exp) {
	return Math.round(num * Math.pow(10, exp)) / Math.pow(10, exp);
}

function countWords(text = '') {
	if (text.replace(/[^a-zA-Zа-яёА-ЯЁ]+/, '') == '') return { counters: {}, total: 0 };

	let splitText = text.split(/[^a-zA-Zа-яёА-ЯЁ]+/),
		counters = {},
		total = splitText.length;

	splitText.forEach(val => {
		val = val.substr(0, 1).toUpperCase() + val.substr(1).toLowerCase();
		if (!counters[val]) counters[val] = 1;
		else counters[val]++;
	});

	if (counters['']) {
		total -= counters[''];
		delete counters[''];
	}

	return { counters: counters, total: total };
}

function drawCountersTable(cWords, allQuantity = 0, column = 0, type = 1) {
	let currentColumn = (['word', 'quantity', 'frequency', 'len'])[column],
		wordsData = [];
	counters.innerHTML = `<tr><th>Word</th><th style='width: 70px;'>Quantity</th><th style='width: 70px;'>Fequency</th><th style='width: 70px;'>Length</th></tr>`;

	Object.keys(cWords).forEach(key => wordsData.push({ word: key, quantity: cWords[key], frequency: numRound(cWords[key] / allQuantity, 5), len: key.length }));

	type = type > 0 ? 1 : -1;
	wordsData.sort((obj1, obj2) => obj1[currentColumn] > obj2[currentColumn] ? type : (obj1[currentColumn] < obj2[currentColumn] ? -type : 0));

	wordsData.forEach(data => counters.innerHTML += `<tr><td>${data.word}</td><td>${data.quantity}</td><td>${data.frequency}</td><td>${data.len}</td></tr>`);
	counters.innerHTML += `<tr><td>#TOTAL:</td><td>${allQuantity}</td></tr>`;

	//сортировка на onclick по шапке талицы
	counters.querySelectorAll('th').forEach((elem, ind) => elem.onclick = () => {
		if (!window.typeCounterSort || !window.typeCounterSort[ind]) window.typeCounterSort = {};
		window.typeCounterSort[ind] = window.typeCounterSort[ind] > 0 ? -1 : 1;
		drawCountersTable(cWords, allQuantity, ind, window.typeCounterSort[ind]);
	});
}

function drawGraphFQ(cWords, allQuantity, ctx, canvas) {
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	ctx.strokeStyle = "#999";
	ctx.lineWidth = 1;
	ctx.beginPath();
	ctx.moveTo(27, 5);
	ctx.lineTo(27, 1005);
	ctx.lineTo(328, 1005);
	ctx.stroke();

	for (let i = 0; i <= 100; i++) {
		ctx.fillText(numRound((100 - i) * 0.01, 2), 2, i * 10 + 9);
		ctx.moveTo((i % 5 > 0 ? 27 : 24), i * 10 + 5);
		ctx.lineTo((i % 5 > 0 ? 29 : 328), i * 10 + 5);
		ctx.stroke();
	}

	for (let i = 0; i <= 30; i++) {
		if (i <= 10 || [15, 20, 25, 30].includes(i)) ctx.fillText(i, i * 10 + (i < 10 ? 25 : 22), 1018);
		ctx.moveTo(i * 10 + 27, (i % 5 > 0 ? 1002 : 5));
		ctx.lineTo(i * 10 + 27, (i % 5 > 0 ? 1005 : 1008));
		ctx.stroke();
	}

	let wordLengthList = {};
	Object.keys(cWords).forEach(word => wordLengthList[word.length] = wordLengthList[word.length] ? wordLengthList[word.length] + cWords[word] : cWords[word]);

	let sorted = Object.keys(wordLengthList).sort().reduce((newarr, key) => { newarr[key] = wordLengthList[key]; return newarr; }, {});
	wordLengthList = sorted;

	Object.keys(wordLengthList).forEach(len => {
		if (Math.min(...Object.keys(wordLengthList)) == len) {
			ctx.strokeStyle = "black";
			ctx.beginPath();
			ctx.lineWidth = 2;
			ctx.moveTo(len * 10 + 27, (1 - wordLengthList[len] / allQuantity) * 1000 + 5);
		}
		else ctx.lineTo(len * 10 + 27, (1 - wordLengthList[len] / allQuantity) * 1000 + 5);
	})
	ctx.stroke();
}

var mytext = document.querySelector('#mytext'),
	counters = document.querySelector('#counters'),
	graphFQ = document.querySelector('#graphFrequencyQuantity'),
	ctxFQ = graphFQ.getContext('2d');

graphFQ.height = 1025;
graphFQ.width = 350;

mytext.addEventListener('input', (event, text = mytext.value) => {
	let words = countWords(text || '');
	drawCountersTable(words.counters, words.total, 0, 1);
	drawGraphFQ(words.counters, words.total, ctxFQ, graphFQ);
});

mytext.dispatchEvent(new Event('input'));