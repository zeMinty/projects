/*
* Функция позволяет нажатием ПКМ по ячейкам
*  окрашивать их в красный и зеленый цвет
*
* Первое нажатие - красный, второе - зеленый
*
* Также есть возможность добавить свои цвета [см. объект colorByButton, стр. 20]
*/

function enable_rightclick_mark() {
    let setColorPair = (p_maskElement, p_clickElement, p_fill=null, p_color=null) => {
        if (p_fill !== null) {
            p_maskElement.setAttribute('fill', p_fill);
        }
        p_clickElement.style.fill = p_color;
    };

    let maskElements = Array.from(document.getElementsByClassName("mask-element"));
    let clickElements = Array.from(document.getElementsByClassName("click-element"));
    let colorByButton = {
        0: { fill:null, color:null },
        2: { fill:['#ddd','#555'], color:['red','green'] },
        else: { fill:'#fff', color:null }
    };

    document.querySelector('svg').oncontextmenu = () => { return false };

    for (const [clickElementIndex, clickElement] of clickElements.entries()) {
        clickElement.onmousedown = event => {
            let maskElement = maskElements[clickElementIndex];
            let currentColor = clickElement.style.fill || null;
            let newColor = colorByButton[event.button] || colorByButton.else;
            let param_fill = newColor.fill;
            let param_color = newColor.color;

            if (Array.isArray(newColor.color)) {
                let ind = newColor.color.indexOf(currentColor);
                param_color = newColor.color[ind+1] || newColor.color[0];
                param_fill = newColor.fill[ind+1] || newColor.fill[0] || newColor.fill;
            }

            setColorPair(maskElement, clickElement, param_fill, param_color);

            return false;
        }
    }

    return 'Enabled.';
}
