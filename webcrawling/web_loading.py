def web_loading(N):
    for _ in tqdm(range(N), total=N, desc='scroll down', leave=True, ncols=100, ascii=True): #블로그 30개 있고, n+=1 때마다 블로그 30개씩 갱신
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)