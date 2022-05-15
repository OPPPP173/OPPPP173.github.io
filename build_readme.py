def fetch_play_time():

    return httpx.get(

        "https://gist.githubusercontent.com/Sanksu/f47f02e2f4f067be39427ed9d76bc9cd/raw/"

    )









    play_time_text = "\n```text\n"+fetch_play_time().text+"\n```\n"



    rewritten = replace_chunk(rewritten, "play_time", play_time_text)

