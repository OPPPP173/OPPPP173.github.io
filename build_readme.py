def fetch_play_time():

    return httpx.get(

        "https://gist.github.com/OPPPP173/c95db24c63b25739d2dad6c189f2b4c7/raw/"

    )









    play_time_text = "\n```text\n"+fetch_play_time().text+"\n```\n"



    rewritten = replace_chunk(rewritten, "play_time", play_time_text)
