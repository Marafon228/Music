// Функция для загрузки и воспроизведения песни по её URL
function loadAndPlaySong(audioSrc) {
    var audio = document.getElementById("myAudio");
    // Остановить предыдущее воспроизведение, если оно было
    audio.pause();
    // Загрузить новый аудиофайл
    audio.src = audioSrc;
    // Воспроизвести песню
    audio.play();

    // Сохранить состояние плеера
    savePlayerState(audio.dataset.songId, 0);
}

// Функция для воспроизведения или паузы аудио
function playPause() {
    var audio = document.getElementById("myAudio");
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
    }
    // Сохранить состояние плеера
    savePlayerState(audio.dataset.songId, audio.currentTime);
}

// Функция для сохранения состояния плеера при его изменении (например, при переходе на другую страницу)
function savePlayerState(songId, currentTime) {
    var playerState = {
        songId: songId,
        currentTime: currentTime
    };
    localStorage.setItem('playerState', JSON.stringify(playerState));
}

// Функция для восстановления состояния плеера
function restorePlayerState() {
    var playerState = loadPlayerState();
    if (playerState) {
        var audioPlayer = document.getElementById('myAudio');
        audioPlayer.dataset.songId = playerState.songId; // Установить ID текущей песни
        loadAndPlaySong(audioPlayer.src); // Загрузить и воспроизвести текущую песню
        audioPlayer.currentTime = playerState.currentTime; // Установить текущее время воспроизведения
    }
}

// Вызов функции для восстановления состояния плеера при загрузке страницы
window.onload = restorePlayerState;
