import asyncio  # You need this for asynchronous sleep
import nodriver as uc  # Assuming nodriver is imported this way
import pandas as pd


async def main():
    # Start the browser session
    browser = await uc.start()

    dff=pd.DataFrame()
    url_df=pd.read_excel('urls_to_scrap.xlsx')
    for url in url_df['URL to Scrap'].to_list():
        print(url)
        page = await browser.get(url)
        content_lst=[]
        for i in range(1,30+1):
            try:
                element = await page.select(f'#socialblade-user-content > div:nth-child(5) > div:nth-child({i})')
                content_text =element.text_all
                content_lst.append(content_text)
                await asyncio.sleep(0.1)  # Correct way to add an asynchronous delay of 1 second  
            except TimeoutError:
                break
        df=pd.DataFrame(content_lst,columns=['main'])
        df[['Date', 'Day', 'Change in Likes', 'Likes', 'Change in Talking About', 'Talking About']] = df['main'].str.split(r'\s+', n=5, expand=True)
        df.drop(columns=['main'], inplace=True)
        df['Likes'] = df['Likes'].str.replace(',', '')
        df['Talking About'] = df['Talking About'].str.replace(',', '')
        df['URL']=url
        dff=pd.concat([dff,df],axis=0)
    return dff

if __name__ == '__main__':
    # Manually create and run the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    df=loop.run_until_complete(main())
    df.to_excel('socialblade.xlsx',index=False)
    