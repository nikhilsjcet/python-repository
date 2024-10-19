''''
Author : Nikhil Saju
Date : 19/10/24
Familiarize time and date in various formats (Eg. “Thu Jul 11 10:26:23 IST 2024”).

    Display current date and time
    Display the format  [YYYY-MM-DD HH:MM:SS]
    Display the format  [MM/DD/YYYY]
    Display the format  [Day, Month DD, YYYY]
    Display the format  [Day, Month DD, YYYY HH:MM:SS AM/PM]
    Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
    Display [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]  Eg: Wed-Oct-02 12:41:18 IST 2024
    Display format- 8 [ISO format:]
    Display Date only
    Display Time only
    Display month only
    Display Year only

Theory

-To work with time and date in various formats in Python, you can use the datetime module.

-This module allows you to format dates and times in different ways using strftime() and parse them using strptime().

Commonly Used Date and Time Format Codes

    %a: Abbreviated weekday name (e.g., Mon, Tue)
    %A: Full weekday name (e.g., Monday, Tuesday)
    %b: Abbreviated month name (e.g., Jan, Feb)
    %B: Full month name (e.g., January, February)
    %d: Day of the month (zero-padded) (e.g., 01, 02, 31)
    %m: Month as a zero-padded decimal number (e.g., 01, 02, 12)
    %Y: Year with century (e.g., 2024)
    %H: Hour (24-hour clock) (e.g., 00, 23)
    %I: Hour (12-hour clock) (e.g., 01, 12)
    %M: Minute as a zero-padded decimal number (e.g., 00, 59)
    %S: Second as a zero-padded decimal number (e.g., 00, 59)
    %p: AM or PM
    %Z: Time zone name (e.g., IST, UTC)
'''





from datetime import datetime
current_time= datetime.now()
print(current_time)
format_1=current_time.strftime("%Y" "%a" "%b" "%B" "%d" "%m" "%H" "%I" "%M" "%S" "%p" "%z")
print(format_1)