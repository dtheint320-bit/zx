import pandas as xz
import streamlit as m
import altair as at

f = m.sidebar.selectbox("Menu", options= ["Played Games Each Years", "Weather Analysis"])

m.set_page_config("Developed By")
m.image("naq.jpg", caption= "@Kevingman3")
m.page_link("https://www.tiktok.com/@kevingman3", label= "My Tiktok Link")



if f == "Played Games Each Years":
    m.title("Most Played Games each 2011-2026 Analysis/Estimated Ranking")

    cd = [2011,
      2012,
      2013,
      2014,
      2015,
      2016,
      2017,
      2018,
      2019,
      2020,
      2021,
      2022,
      2023,
      2024,
      2025,
      2026]

    bc= m.selectbox("Select Year", cd)

    if bc == cd[0]:
        m.header("Most Played Games in 2011")
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League Of Legends"],
                   "Players Count": [16, 9, 6.7, 33],
                   "Players": ["16M", "9M", "6.7M", "33M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N",
                                             title= "Most Played Games"), 
                                             y= at.Y("Players Count:Q",
                                                      title= "Total Players Of Each Years",
                                                        axis= at.Axis(labelExpr= "datum.value + 'M'")
                                                        ),
                                                         tooltip= [at.Tooltip('Players:N' )]).properties(width = 300, height = 300)
        
        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2011🏆:" "League Of Legends")


    if bc == cd[1]:
        m.header("Most Played games in 2012")
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [23, 12.1, 12, 42],
                   "Players": ["23M", "12.1M", "12M", "42M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2012🏆:" "League Of Legends")

    if bc == cd[2]:
        m.header("Most Played games in 2013")
      
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [36, 16.7, 17.2, 67],
                   "Players": ["36M", "16.7M", "17.2M", "67M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2013🏆:" "League Of Legends")

    if bc == cd[3]:
        m.header("Most Played games in 2014")

        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [60, 24, 22, 67],
                   "Players": ["60M", "24M", "22M", "67M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2014🏆:" "League Of Legends")

    if bc == cd[4]:
        m.header("Most Played games in 2015")

        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [83, 29, 27, 100],
                   "Players": ["83M", "29M", "27M", "100M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2015🏆:" "League of Legends")

    if bc == cd[5]:
        m.header("Most Played games in 2016")

        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [100.15, 36, 34, 100],
                   "Players": ["100.15M", "36M", "34M", "100M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2016🏆:" "Minecraft")
    

    if bc == cd[6]:
        m.header("Most Played games in 2017")

        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends"],
                   "Players Count": [110, 51.3, 38, 100],
                   "Players": ["110M", "51.3M", "38M", "100M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2017🏆:" "Minecraft")
    

    if bc == cd[7]:
        m.header("Most Played games in 2018")

        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends", "PUBG", "Fortnite"],
                   "Players Count": [120, 67, 37, 100, 89, 30],
                   "Players": ["120M", "67M", "37M", "100M", "89M", "30M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2018🏆:" "Minecraft")

    if bc == cd[8]:
        m.header("Most Played games in 2019")
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "Counter Strike", "League of Legends", "PUBG", "Fortnite", "Among Us"],
                   "Players Count": [125, 112, 46, 115, 89, 30, 20],
                   "Players": ["125M", "112M", "46M", "115M", "89M", "30M", "20M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2019🏆:" "Minecraft")
        

    if bc == cd[9]:
        m.header("Most Played games in 2020")
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us"],
                   "Players Count": [131, 75, 114, 300, 250, 500],
                   "Players": ["131M", "75M", "114M", "300M", "250M", "500M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2020🏆:" "Among Us")



    if bc == cd[10]:
        m.header("Most Played games in 2021")
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [141, 200, 180, 340, 343, 70, 54],
                   "Players": ["141M", "200M", "180M", "340M", "343M", "70M", "54M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2021🏆:" "Fortnite")

    if bc == cd[11]:
        m.header("Most Played games in 2022")
       
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [179, 220, 152, 290, 246, 40, 64],
                   "Players": ["179M", "220M", "152M", "290M", "246M", "40M", "64M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)

        m.header("Top for 2022🏆:" "PUBG")

    if bc == cd[12]:
        m.header("Most Played games in 2023")
        
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [170, 270, 154, 320, 243, 24, 66],
                   "Players": ["170M", "270M", "154M", "320M", "243M", "24M", "66M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2023🏆:" "PUBG")
        


    if bc == cd[13]:
        m.header("Most Played games in 2024")
       
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [181, 340, 164, 310, 240, 30, 64],
                   "Players": ["181M", "340M", "164M", "310M", "240M", "30M", "64M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2024🏆:" "Roblox")


    if bc == cd[14]:
        m.header("Most Played games in 2025")
        
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [193, 390, 175, 323, 268, 23, 56],
                   "Players": ["193M", "390M", "175M", "323M", "268M", "23M", "56M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2025🏆:" "Roblox")
    
    
    if bc == cd[15]:
        
        m.header("Most Played games in 2026")
        
        xs = xz.DataFrame({"Games": ["Minecraft", "Roblox", "League of Legends", "PUBG", "Fortnite", "Among Us", "Genshin Impact"],
                   "Players Count": [200, 420, 176, 332, 284, 17, 56],
                   "Players": ["200M", "420M", "176M", "332M", "284M", "17M", "56M"]})

        vc = at.Chart(xs).mark_bar().encode(x= at.X("Games:N", title= "Most Played Games"),
                                         y = at.Y("Players Count:Q", 
                                                  title= "Players",
                                                    axis= at.Axis(labelExpr= "datum.value + 'M'")), 
                                                    tooltip= at.Tooltip("Players:N", title= "Players")).properties(width = 300, height = 300)

        m.altair_chart(vc, use_container_width= True)
        m.header("Top for 2026🏆:" "Roblox")

    xc, mv, cg, vs = m.columns(4)

    with xc:
        m.metric("Minecraft Most Played/Peak Year", 
             value= "2026", 
             delta= "200M")

    with mv:
        m.metric("Minecraft Least Played/Worst Year",
             value= "2011",
             delta= "5-10M",
             delta_color= "inverse")

    with cg:
        m.metric("Roblox Most Played/Peak Year",
                 value= "2026",
                 delta= "420M",)
        
    with vs:
        m.metric("Roblox Least Played/Worst Year",
                 value= "2011",
                 delta= "5-10M",
                 delta_color= "inverse")
        
    pc, vb, hj, li = m.columns(4)
    with pc:
        m.metric("League Of Legends Most Played/Peak Year", 
             value= "2025-2026", 
             delta= "170-180M")

    with vb:
        m.metric("League Of Legends Least Played/Worst Year",
                 value= "2011",
                 delta= "30-35M",
                 delta_color= "inverse")
        
    with hj:
        m.metric("PUBG Most Played/Peak Year", 
             value= "2020/2021", 
             delta= "300-350M")

    with li:
        m.metric("PUBG Least Played/Worst Year", 
             value= "2017", 
             delta= "80-100M",
             delta_color= "inverse")
        

    
    ec, vd, py, rd = m.columns(4)

    with ec:
        m.metric("Fortnite Most Played/Peak Year", 
                 value= "2021",
                   delta= "300-350")
        
    with vd:
        m.metric("Fortnite Least Played/Worst Year", 
             value= "2017", 
             delta= "20-30M",
             delta_color= "inverse")
        
    with py:
        m.metric("Among Us Most Played/Peak Year", 
                 value= "2020",
                   delta= "500M")
        
    with rd:
        m.metric("Fortnite Least Played/Worst Year", 
             value= "2019", 
             delta= "5-10M",
             delta_color= "inverse")
        
    jds, mac = m.columns(2)

    with jds:
        m.metric("Genshin Imapct Most Played/Peak Year", 
                 value= "60-65",
                   delta= "500M")
        

    with mac:
        m.metric("Genshin Impact Least Played/Worst Year", 
             value= "2020", 
             delta= "40-50",
             delta_color= "inverse")

if f == "Weather Analysis":
    
    g = xz.DataFrame({"Years": [2021, 2022, 2023, 2024, 2025],
                      "Degrees": [1.2, 1.23, 1.4, 1.67, 1.65],
                      "CI": ["1.2°C", "1.23°C", "1.4°C", "1.67°C", "1.65°C"]})
    
    f = at.Chart(g).mark_line().encode(x= at.X("Years:O",title= "Years" ), 
                                       y= at.Y("Degrees:Q", 
                                               title= "Degrees",
                                                
                                               axis= at.Axis(labelExpr= "datum.value + '°C'")), 
                                               tooltip= at.Tooltip("CI:N", title= "Degrees")
                                                

                                               ).properties(width = 400, 
                                                                                             height = 423)

    m.altair_chart(f, use_container_width= True)

