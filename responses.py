def sample_response(parm):
    user_command = str(parm).lower()

    if user_command in ('hey', 'hello', 'sup',):
        return """
                Hey there!!!!
            """
    if user_command in ('sections'):
        return """
        Hello, These are the sections we have
        1) Syllabus
        2) Video Library 
        **PLEASE BE SURE YOU ENTER THEM EXACTLY AS STATED"""

    if user_command in ('who are you?', 'can i know you?', 'who are you', 'can i know u',):
        return "I am a bot set by A level student from Nepal to help guide students in A level mathematics"

    if user_command in ("syllabus"):
        return "https://www.cambridgeinternational.org/Images/415060-2020-2022-syllabus.pdf"

    if user_command in ('videolibrary', 'video library'):
        return """pure Mathematics 1
            pure Mathematics 2/3
            Mechanics
            Probability and Statistics 1
            Probability and Statistics 2
        """

    if user_command in ("pure mathematics 1"):
        return """
        topics:
        1) Quadratics 1
        2) Functions 1
        3) Coordinate Geometry 1
        4) Circular Measure 1
        5) Differentiation 1
        6) Integration 1
        7) Sequence and Series 1
        
        View the playlist here: 
        https://www.youtube.com/playlist?list=PLLyqGZba3Xv2QFDhg6BCzvjDW0Use8_mD
        """

    if user_command in ("pure mathematics 2/3"):
        return """
        yet to come Stay tuned!!!!!!!
        """

    if user_command in ("mechanics"):
        return """
        Here is a playlist for Mechanics:
        https://www.youtube.com/playlist?list=PLLyqGZba3Xv0dk0CsCK-ua95z4i_eFzF8
        """
    if user_command in ("probability and statistics 1"):
        return """
        Here is a playlist for Probability and Statistics 1
        https://youtube.com/playlist?list=PLLyqGZba3Xv20VTzd1j_0jIe_J44VqcbX
        """

    if user_command in ("quadratics 1"):
        return "https://youtu.be/Ia7nJO10xi8"

    if user_command in ("functions 1"):
        return """https://www.youtube.com/watch?v=uXjVTZFq7nQ
        or 
        https://youtube.com/playlist?list=PLLyqGZba3Xv3UWqAGlJkVQZvb8s4WLm_u
        """

    if user_command in ("coordinate geometry 1"):
        return """https://www.youtube.com/watch?v=wl_p32llVTU"""

    if user_command in ("circular measure 1"):
        return "https://www.youtube.com/playlist?list=PLLyqGZba3Xv0LErDHeZmtGi6bvznKZLQy"

    if user_command in ("differentiation 1"):
        return "https://youtube.com/playlist?list=PLLyqGZba3Xv1si0XKtp_91LmYwlwQQKAC"

    if user_command in ("integration 1"):
        return "https://www.youtube.com/playlist?list=PLLyqGZba3Xv3gxFwvV5UiwtthZ2mA1hcc"

    if user_command in ("sequence and series 1"):
        return "https://youtube.com/playlist?list=PLLyqGZba3Xv2pbitWGtK4rsMmlPaLCQp3"





