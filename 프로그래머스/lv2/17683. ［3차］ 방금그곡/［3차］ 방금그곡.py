from datetime import datetime

def solution(m, musicinfos):
    answer = "(None)"
    max_play_time = 0
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        start_time = datetime.strptime(info[0], "%H:%M")
        end_time = datetime.strptime(info[1], "%H:%M")
        play_time = (end_time - start_time).total_seconds() / 60
        title = info[2]
        melody = info[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        # 멜로디를 재생 시간에 맞게 확장
        full_melody = (melody * int(play_time / len(melody))) + melody[:int(play_time % len(melody))]

        # 멜로디 m이 악보에 있는 경우
        if m in full_melody:
            if play_time > max_play_time:
                max_play_time = play_time
                answer = title

    return answer
