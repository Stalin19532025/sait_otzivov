// скрипт ниже будет обновлять картинку поста при загрузке новой
document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("новый_файл");
    const preview = document.getElementById("картинка_поста");
    // чтобы скрипт понимал, какие элементы нужно менять, необходимо привязать id к тегу в хтмл и здесь скопировать его имя

    input.addEventListener("change", function () {
        const файл = this.files[0];
        if (файл) {
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
            };
            reader.readAsDataURL(файл);
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Наша кука начинается с имени
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function confirmRedirect(linkElement) {
    if (confirm("Вы уверены?")) {
        return true;
    } else {
        return false;
    }
}