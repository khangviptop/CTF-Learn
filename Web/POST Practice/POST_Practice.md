# POST Practice ❓
**Tags:** Web Exploitation<br>
**Point:** 40<br>
**Level:** Medium<br>
**Description:** 
This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php

## Write-up: 📝
The description above shows the most information we have to do. In conclusion, we just have to find out the way to post a available payload to the website to obtain the flag.
### Solution: 💯
```
1. The hint in this challenge is given in description. 
2. The method originally sent to website is GET. So we try POST to get through this challenge.
(We can check it by using BurpSuite)
3. Remember the payload is viewed when inspecting element
<!-- username: admin | password: 71urlkufpsdnlkadsf -->
4. We have two solution 3 solution to solve this
● Using BurpSuite
● Code by Python with built-in modules (Requests)
● Command (a.k.a bash language for shell)
```

#### The Flag (for reference): ✔️
```
CTFlearn{p0st_d4t4_4ll_d4y}
```
