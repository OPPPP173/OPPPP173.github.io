def fetch_play_time():

    return httpx.get(

        "https://gist.github.com/OPPPP173/3d0fa8da2f69931cb499fc673f53f1af/raw/"

    )









    play_time_text = "\n```text\n"+fetch_play_time().text+"\n```\n"



    rewritten = replace_chunk(rewritten, "play_time", play_time_text)

