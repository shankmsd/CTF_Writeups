## Challenge 🧩

We captured enemy spy and intercepted a message. According to our crypt analysts, it's encrypted with an unbreakable cipher. Fortunately, the spy lacks key management skills and carried this key: "VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg==". We sent you a copy of the message. Decrypt it. Your password is "Sidney".
Remember, connect to your terminal with the command:

```shell
socat file:`tty`,rawer tcp:otp0.2023-bq.ctfcompetition.com:1337
```

HINT: Decode the key first.

## Solution 🕵️‍♂️

First we will decode the key carried by spy.

![Base64 Decode](src/C0_Base64_Decode.PNG)

Connecting Terminal

```shell
socat file:`tty`,rawer tcp:otp0.2023-bq.ctfcompetition.com:1337
```

After, we will prompted for password use `Sidney` as password

![Password Screen](src/C0_Password_Screen.PNG)

![Welcome Screen](src/C0_Welcome_Screen.PNG)

Next, Navigate to Spam folder

![Encrypted Spam Folder](src/C0_Encrypted_Spam_Folder.PNG)

Press Enter to access the folder

![Secret Key Prompt](src/C0_Secret_Key_Prompt.PNG)

Use the decoded key
> `The Venona project was a United States counterintelligence program initiated during World War II`

![Message with Flag](src/C0_Message_with_Flag.PNG)

## Flag 🚩

`CTF{Ace_of_Spies}`
