function readVar(helpStr, storeStr) {
    let psId = prompt(helpStr);
    if (!psId) {
        alert('输入不得为空！');
        readVar(helpStr, storeStr);
    } else {
        localStorage.setItem(storeStr, psId);
        // alter here
        alert('succeed!');
    }
}

// let btn1 = document.getElementById('btn1');
let btn2 = document.getElementById('btn2');

// btn1.onclick = function() {
//     readVar('Problemset序列号(仅数字):', 'psId');
//     readVar('Problem题号(仅大写字母):', 'pId');
// }

btn2.onclick = function() {
    readVar('用户昵称:', 'userName');
    document.getElementById('user_name').value = localStorage.getItem('userName');
}