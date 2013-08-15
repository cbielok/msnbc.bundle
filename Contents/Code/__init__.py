MSNBC_NAMESPACE   = {'v':'http://www.w3.org/2005/Atom', 'media':'http://search.yahoo.com/mrss/'}
MSNBC_URL         = 'http://rss.msnbc.msn.com/id/'
LATEST_URL        = 'http://podcastfeeds.nbcnews.com/audio/podcast/%s.xml' #path

PREFIX = "/video/msnbc",

ART = 'art-default.jpg'
ICON = 'icon-default.jpg'

# rss feeds for the main menu shows
RSS_SHOWS = [
  {'title'  : 'All In',                 'link'  : '51362794/device/rss/vp/3096434'},  {'title'  : 'Andrea Mitchell Reports','link'  : '34510812/device/rss/vp/3096434'},
  {'title'  : 'The Cycle',              'link'  : '47905980/device/rss'},             {'title'  : 'Daily Rundown',          'link'  : '34419168/device/rss/vp/3096434'},
  {'title'  : 'Dateline',               'link'  : '18424719/device/rss/'},            {'title'  : 'The Dylan Ratigan Show', 'link'  : '34419165/device/rss/vp/3096434'},
  {'title'  : 'The Ed Show',            'link'  : '30012522/device/rss/vp/3096434'},  {'title'  : 'Jansing & Co',           'link'  : '41894601/device/rss'},
  {'title'  : 'The Last Word',          'link'  : '38865210/device/rss/vp/3096434'},  {'title'  : 'Martin Bashir',          'link'  : '41894607/device/rss/'},
  {'title'  : 'Melissa Harris-Perry',   'link'  : '46404075/device/rss/vp/47722962'}, {'title'  : 'MSNBC TV',               'link'  : '18424721/device/rss/vp/3096434'},
  {'title'  : 'Politics Nation',        'link'  : '47728749/device/rss/vp/45755884'}, {'title'  : 'Up With Steve Kornacki', 'link'  : '44507040/device/rss/vp/46979738'},
  {'title'  : 'Way Too Early',          'link'  : '32178079/device/rss/vp/3096434'},  {'title'  : 'Weekends with Alex Witt','link'  : '51071113/device/rss'}
]
# rss feeds for the Rachel Maddow Show 
MADDOW_FEEDS = [
  {'title'  : 'Latest Programs',  'link'  : '27668917/device/rss/vp/26315908'}, {'title'  : 'Most Viewed',   'link'  : '27108530/device/rss/vp/26315908'},
  {'title'  : 'Ms. Information',  'link'  : '26776800/device/rss/vp/26315908'}, {'title'  : 'GOP in Exile',  'link'  : '28937296/device/rss/vp/26315908'},
  {'title'  : 'Rachel Re:',       'link'  : '26776790/device/rss/vp/26315908'}, {'title'  : 'Just Enough',   'link'  : '26776791/device/rss/vp/26315908'},
  {'title'  : 'Recommended',      'link'  : '27351114/device/rss/vp/26315908'}
]
# rss feeds for the Nightly News
NIGHTLY_NEWS = [
  {'title'  : 'Full Episodes',        'link'  : '18424748/device/rss'}, {'title'  : 'Latest Program',     'link'  : '22422632/device/rss'},
  {'title'  : 'Most Viewed',          'link'  : '22453546/device/rss'}, {'title'  : 'Brian Williams',     'link'  : '21437648/device/rss'},
  {'title'  : 'Politics',             'link'  : '21677453/device/rss'}, {'title'  : 'Hard Times',         'link'  : '24856627/device/rss'},
  {'title'  : 'Health',               'link'  : '22827958/device/rss'}, {'title'  : 'World News',         'link'  : '22827879/device/rss'},
  {'title'  : 'Weather',              'link'  : '26676833/device/rss'}, {'title'  : 'Our Planet',         'link'  : '21437577/device/rss'},
  {'title'  : 'Making a Difference',  'link'  : '21437535/device/rss'}, {'title'  : 'In Their Own Words', 'link'  : '21437630/device/rss'}
]
# rss feeds for the Nightly News - "web only" content
NN_WEB  = [
  {'title'  : 'Latest Clips',             'link'  : '22316432/device/rss'}, {'title'  : 'Extended Interviews',  'link'  : '22423188/device/rss'},
    {'title'  : 'NBC Behind the Scenes',  'link'  : '23018885/device/rss'}, {'title'  : 'Digital Dispach',      'link'  : '21550471/device/rss'}
]
# rss feeds for Meet The Press
MEET_THE_PRESS = [
  {'title'  :   'Full Episodes',        'link'  :   '18424745/device/rss'}, {'title'    :   'Latest Clips',         'link'  :   '18424744/device/rss'},
  {'title'  :   'Insights & Analysis',  'link'  :   '21437686/device/rss'}, {'title'    :   'News Makers',          'link'  :   '21437662/device/rss'},
  {'title'  :   'Take Two',             'link'  :   '21437717/device/rss'}, {'title'    :   'Meet The Candidates',  'link'  :   '21437695/device/rss'},
  {'title'  :   '60th Anniversary',     'link'  :   '22410986/device/rss'}, {'title'    :   'Russert Remembered',   'link'  :   '25146060/device/rss'}
]
# rss feeds for the Today Show - "Latest Program"
TS_LATEST = [
  {'title'  :   'Latest Clips',  'link'  : '18424824/device/rss/vp/26184891'}, {'title'  : 'Honda & Cathy Lee', 'link'  :  '26316687/device/rss/vp/26184891'}
]
# rss feeds for Today Show - News
TS_NEWS = [
  {'title'  :  'Latest Clips',       'link'  :  '22828010/device/rss/vp/26184891'},  {'title'  :  'Politics',  'link'  :  '25274211/device/rss/vp/26184891'},
  {'title'  :  'Tales of Survival',  'link'  :  '26316706/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Concert Series
TS_CONCERT = [
  {'title'  :  'Latest Clips',  'link'  :  '21659048/device/rss/vp/26184891'},  {'title'  :  'Backstage Pass',  'link'  :  '25723585/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Diet & Health
TS_DIET = [
  {'title'  :  'Latest Clips',  'link'  :  '22828130/device/rss/vp/26184891'},  {'title'  :  'Nutrition with Joy Bauer',  'link'  :  '25887307/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Entertainment
TS_ENTERTAINMENT = [
  {'title'  :  'Latest Clips',  'link'  :  '21658676/device/rss/vp/26184891'},  {'title'  :  'Critics Class',  'link'  :  '26316665/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Fashion
TS_FASHION = [
  {'title'  :  'Latest Clips',  'link'  :  '21658676/device/rss/vp/26184891'},  {'title'  :  'Ambush Makeovers',  'link'  :  '25887326/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Relationships
TS_WEDDINGS = [
  {'title'  :  'Latest Clips',  'link'  :  '21658957/device/rss/vp/26184891'},  {'title'  :  'Wedding',  'link'  :  '21659067/device/rss/vp/26184891'}
]
# rss feeds for Today Show - Special Features
TS_SPECIAL = [
  {'title'  :  'Anchor Roots',      'link'  :  '26408377/device/rss/vp/26184891'},  {'title'  :  'Where in the World',  'link'  :  '21659089/device/rss/vp/26184891'},
  {'title'  :  'Today in Beijing',  'link'  :  '25854156/device/rss/vp/26184891'},  {'title'  :  'Ends of the Earth',   'link'  :  '21636851/device/rss/vp/26184891'}
]
# rss feeds for Today Show
TODAY_SHOW = [
  {'title'  :  'Most Viewed',           'link'  :  '18424824/device/rss/vp/26184891'},  {'title'  :  'Previously',      'link'  :  '26411480/device/rss/vp/26184891'},
  {'title'  :  'Food & Wine',           'link'  :  '21658719/device/rss/vp/26184891'},  {'title'  :  'Home & Garden',   'link'  :  '21658803/device/rss/vp/26184891'},
  {'title'  :  'Money',                 'link'  :  '23152698/device/rss/vp/26184891'},  {'title'  :  'Parenting',       'link'  :  '21658914/device/rss/vp/26184891'},
  {'title'  :  'Favorite People: 2008', 'link'  :  '28357213/device/rss/vp/26184891'},  {'title'  :  'Pets',            'link'  :  '23152689/device/rss/vp/26184891'},
  {'title'  :  'People',                'link'  :  '29411569/device/rss/vp/26184891'},  {'title'  :  'Tech & Gadgets',  'link'  :  '23152694/device/rss/vp/26184891'},
  {'title'  :  'Travel',                'link'  :  '22828279/device/rss/vp/26184891'},  {'title'  :  'Web-only',        'link'  :  '21658973/device/rss/vp/26184891'}
]
# rss feeds for Morning Joe
MORNING_JOE = [
  {'title'  :  'Most Viewed',           'link'  :  '28184433/device/rss/vp/28159725'},  {'title'  :  'Politics',    'link'  :  '28184154/device/rss/vp/28159725'},
  {'title'  :  'News You Can\'t Use',   'link'  :  '28184451/device/rss/vp/28159725'},  {'title'  :  'Economy',     'link'  :  '28184592/device/rss/vp/28159725'},
  {'title'  :  'Health Care',           'link'  :  '30314086/device/rss/vp/28159725'},  {'title'  :  'Scoop',       'link'  :  '28184387/device/rss/vp/28159725'},
  {'title'  :  'Best of Morning Joe',   'link'  :  '28117873/device/rss/vp/28159725'}
]
# rss feeds for ZeitGeist
ZEITGEIST = [
  {'title'  :  'Latest Clips',  'link'  :  '20418176/device/rss/vp/26852192'},  {'title'  :  'Most Viewed',   'link'  :  '27707215/device/rss/vp/26852192'},
  {'title'  :  'Willie on TV',  'link'  :  '25196846/device/rss/vp/26852192'}
]
# rss feeds for Hardball
HARDBALL = [
  {'title'  :  'Latest Clips',  'link'  :  '29058318/device/rss/vp/29279101'},  {'title'  :  'Most Viewed',     'link'  :  '29058303/device/rss/vp/29279101'},
  {'title'  :  'Newsmakers',    'link'  :  '29058145/device/rss/vp/29279101'},  {'title'  :  'Politics Fix',    'link'  :  '29058233/device/rss/vp/29279101'},
  {'title'  :  'Slideshow',     'link'  :  '29058266/device/rss/vp/29279101'},  {'title'  :  'Big Number',      'link'  :  '29058274/device/rss/vp/29279101'}
]
# rss feeds for US News
NEWS_US = [
  {'title'  :  'Latest Clips',      'link'  :  '21426262/device/rss'},  {'title'  :  'Crime & Courts',      'link'  :  '21427653/device/rss'},
  {'title'  :  'Education',         'link'  :  '23600346/device/rss'},  {'title'  :  'The Elkhart Project', 'link'  :  '29637267/device/rss'},
  {'title'  :  'Environment',       'link'  :  '21427657/device/rss'},  {'title'  :  'Faith"',              'link'  :  '23600340/device/rss'},
  {'title'  :  'Life"',             'link'  :  '21427662/device/rss'},  {'title'  :  'Military',            'link'  :  '21427669/device/rss'},
  {'title'  :  'Race & Ethnicity',  'link'  :  '21427673/device/rss'},  {'title'  :  'Security',            'link'  :  '21427678/device/rss'},
  {'title'  :  'Weird News',        'link'  :  '18424731/device/rss'}
]
# rss feeds for World News
NEWS_WORLD = [
  {'title'  :  'Latest Clips',          'link'  :  '21426473/device/rss'},  {'title'  :  'Americas',                'link'  :  '21427766/device/rss'},
  {'title'  :  'Africa',                'link'  :  '21427760/device/rss'},  {'title'  :  'Asia-Pacific',            'link'  :  '21427768/device/rss'},
  {'title'  :  'Conflict in Iraq',      'link'  :  '21427754/device/rss'},  {'title'  :  'Europe',                  'link'  :  '21427850/device/rss'},
  {'title'  :  'South & Central Asia',  'link'  :  '21427861/device/rss'},  {'title'  :  'Middle East & N. Africa', 'link'  :  '21427857/device/rss'},
  {'title'  :  'Terrorism',             'link'  :  '21427756/device/rss'},  {'title'  :  'Wonderful World',         'link'  :  '21427651/device/rss'}
]
# rss feeds for Business News
NEWS_BUSINESS = [
  {'title'  :  'Latest Clips',  'link'  :  '18424694/device/rss'},  {'title'  :  'Stock and Economy',   'link'  :  '21427890/device/rss'},
  {'title'  :  'U.S. Business', 'link'  :  '21427903/device/rss'},  {'title'  :  'Autos',               'link'  :  '21427924/device/rss'},
  {'title'  :  'Real Estate',   'link'  :  '21427971/device/rss'},  {'title'  :  'Retail',              'link'  :  '21427996/device/rss'},
  {'title'  :  'Careers',       'link'  :  '21427991/device/rss'},  {'title'  :  'Personal Finance',    'link'  :  '21427918/device/rss'},
  {'title'  :  'Small Business','link'  :  '21427920/device/rss'},  {'title'  :  'Your Business',       'link'  :  '18424833/device/rss'}
]
# rss feeds for Politics News
NEWS_POLITICS = [
  {'title'  :  'Latest Clips',  'link'  :  '18424734/device/rss'},  {'title'  :  'The White House',  'link'  :  '21427723/device/rss'},
  {'title'  :  'Capitol Hill',  'link'  :  '21427731/device/rss'}
]
# rss feeds for Entertainment News
NEWS_ENTERTAINMENT = [
  {'title'  :  'Latest Clips',      'link'  :  '18424692/device/rss'},  {'title'  :  'Access Hollywood',  'link'  :  '20418142/device/rss'},
  {'title'  :  'Celebrities',       'link'  :  '21428100/device/rss'},  {'title'  :  'Keeping Tabs',      'link'  :  '20498047/device/rss'},
  {'title'  :  'Lifestyle',         'link'  :  '21428119/device/rss'},  {'title'  :  'Movies',            'link'  :  '18424697/device/rss'},
  {'title'  :  'Music',             'link'  :  '21428116/device/rss'},  {'title'  :  'Television',        'link'  :  '21428108/device/rss'},
  {'title'  :  'Scoop',             'link'  :  '28184387/device/rss/vp/28159725'}
]
# rss feeds for Health News
NEWS_HEALTH = [
  {'title'  :  'Latest Clips',      'link'  :  '21427299/device/rss'},  {'title'  :  'Aging',             'link'  :  '21428203/device/rss'},
  {'title'  :  'Animal Tracks',     'link'  :  '18424682/device/rss'},  {'title'  :  'Cancer',            'link'  :  '21428191/device/rss'},
  {'title'  :  'Diet & Nutrition',  'link'  :  '21428136/device/rss'},  {'title'  :  'Fitness',           'link'  :  '21428178/device/rss'},
  {'title'  :  'Food Safety',       'link'  :  '30018791/device/rss'},  {'title'  :  'Health Care',       'link'  :  '30018753/device/rss'},
  {'title'  :  'Heart Health',      'link'  :  '21428183/device/rss'},  {'title'  :  'Kids & Parenting',  'link'  :  '21428155/device/rss'},
  {'title'  :  'Men\'s Health")',   'link'  :  '21428151/device/rss'},  {'title'  :  'Mental Health',     'link'  :  '21428162/device/rss'},
  {'title'  :  'Pet Health',        'link'  :  '21428208/device/rss'},  {'title'  :  'Sexual Health',     'link'  :  '21428170/device/rss'},
  {'title'  :  'Skin & Beauty',     'link'  :  '21480182/device/rss'},  {'title'  :  'Women\'s Health',   'link'  :  '21428143/device/rss'}
]
# rss feeds for Sports News
NEWS_SPORTS = [
  {'title'  :  'Latest Sports',     'link'  :  '21426493/device/rss'},                              {'title'  :  'MMA',             'link'  :  'http://nbcsports.msnbc.com/id/21428080/device/rss'},
  {'title'  :  'MLB',               'link'  :  'http://nbcsports.msnbc.com/id/21428015/device/rss'},{'title'  :  'NASCAR/Motors',   'link'  :  'http://nbcsports.msnbc.com/id/22114938/device/rss'},
  {'title'  :  'NBA',               'link'  :  'http://nbcsports.msnbc.com/id/21428039/device/rss'},{'title'  :  'NCAA Football',   'link'  :  'http://nbcsports.msnbc.com/id/21428047/device/rss'},
  {'title'  :  'NCAA Hoops',        'link'  :  'http://nbcsports.msnbc.com/id/21428068/device/rss'},{'title'  :  'NFL',             'link'  :  'http://nbcsports.msnbc.com/id/21428022/device/rss'},
  {'title'  :  'NHL',               'link'  :  'http://nbcsports.msnbc.com/id/21428025/device/rss'},{'title'  :  'PGA',             'link'  :  'http://nbcsports.msnbc.com/id/21428026/device/rss'},
  {'title'  :  'Horse Racing',      'link'  :  'http://nbcsports.msnbc.com/id/21428075/device/rss'},{'title'  :  'Tennis',          'link'  :  'http://nbcsports.msnbc.com/id/21428033/device/rss'},
  {'title'  :  'Sports Oddities',   'link'  :  'http://nbcsports.msnbc.com/id/23017283/device/rss'},{'title'  :  'Mad Dog Minute',  'link'  :  'http://nbcsports.msnbc.com/id/23017809/device/rss'},
  {'title'  :  'Matty Blake',       'link'  :  'http://nbcsports.msnbc.com/id/23258082/device/rss'}
]
# rss feeds for Tech News
NEWS_TECH = [
  {'title'  :  'Latest Clips',  'link'  :  '18424747/device/rss'},  {'title'  :  'Games',               'link'  :  '26560891/device/rss'},
  {'title'  :  'Science',       'link'  :  '21428316/device/rss'},  {'title'  :  'Space',               'link'  :  '18424741/device/rss'},
  {'title'  :  'Technology',    'link'  :  '21428240/device/rss'},  {'title'  :  'Red Tape Chronicals', 'link'  :  '28780760/device/rss'}
]
# rss feeds for Travel News
NEWS_TRAVEL = [
  {'title'  :  'Latest Clips',  'link'  :  '21427411/device/rss'},  {'title'  :  'Travel Tips',  'link'  :  '26560980/device/rss'}
]
# rss feeds for Weather
WEATHER = [
  {'title'  :  'Latest Clips',          'link'  :  '25198763/device/rss'},  {'title'  :  'National Forecasts',    'link'  :  '30331543/device/rss'},
  {'title'  :  'Regional Forecasts',    'link'  :  '30331544/device/rss'},  {'title'  :  'Top Local Forecasts',   'link'  :  '30331545/device/rss'},
  {'title'  :  'Vacation Forecasts',    'link'  :  '30331546/device/rss'},  {'title'  :  'Forecast Earth',        'link'  :  '30331549/device/rss'},
  {'title'  :  'Epic Conditions',       'link'  :  '30332550/device/rss'},  {'title'  :  'Weather Changed History','link'  :  '30331551/device/rss'}
]


###################################################################################################
def Start():
  ObjectContainer.title1 = 'MSNBC'
  ObjectContainer.art = R(ART)
  DirectoryObject.thumb = R(ICON)

###################################################################################################
@handler(PREFIX, 'MSNBC', thumb=ICON, art=ART)
def MainMenu():
  oc = ObjectContainer()
  oc.add(DirectoryObject(key=Callback(News), title="All News"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=HARDBALL, title2="Hardball", thumb='meet_the_press.png',
    title="Hardball", thumb=R('hardball.jpeg')))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=MEET_THE_PRESS, title2="Meet The Press", thumb='meet_the_press.png',
    latest_episode='MSNBC-MTP-NETCAST-M4V'), title="Meet The Press", thumb=R('meet_the_press.png')))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=MORNING_JOE, title2="Morning Joe", thumb='joe.png',
    latest_episode='MSNBC-SCARBOROUGH-NETCAST-M4V'), title="Morning Joe", thumb=R('joe.png')))
  oc.add(DirectoryObject(key=Callback(Nightly_News), title="Nightly News with Brian Williams", thumb=R('nightly_news.png')))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=MADDOW_FEEDS, title2='The Rachel Maddow Show', thumb='maddow.png',
    latest_episode='MSNBC-MADDOW-NETCAST-M4V'), title="The Rachel Maddow Show", thumb=R('maddow.png')))
  oc.add(DirectoryObject(key=Callback(Today), title="Today Show", thumb=R('today.png')))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=ZEITGEIST, title2="ZeitGeist", thumb='zeitgeist.png'),
    title="ZeitGeist", thumb=R('zeitgeist.png')))
  oc.extend(FeedDirectory(feed_list=RSS_SHOWS))
  oc.objects.sort(key = lambda obj: obj.title)
  return oc

###################################################################################################
@route(PREFIX + '/videorss')
def GetVideosRSS(rss_url, title1='MSNBC', title2='Videos'):
  oc = ObjectContainer(titl1=title1, title2=title2)
  if not rss_url.startswith('http://'):
    rss_url = MSNBC_URL + rss_url
  feed = RSS.FeedFromURL(rss_url)
  default_thumb = feed.image
  for video in feed.entries:
    title = video.title
    summary = video.description
    date = video.updated
    link = video.link
    duration = Datetime.MillisecondsFromString(video.itunes_duration)
    try:
      thumb = video.image
    except:
      thumb = default_thumb
    oc.add(VideoClipObject(url=link, title=title, summary=summary, originally_available_at=date, duration=duration,
      thumb=Resource.ContentsOfURLWithFallback(url=thumb.replace('.thumb.jpg', '.ss_full.jpg'), fallback=thumb)))

  if len(oc) < 1:
    return ObjectContainer(header="Empty Directory", message="There is no content to display.")
  
  return oc
   
###################################################################################################
@route(PREFIX + '/feeds', feed_list=list)
def FeedDirectory(feed_list, title1='MSNBC',title2='Feeds',thumb=ICON, latest_episode=None):
  oc = ObjectContainer(title1=title1, title2=title2)
  if latest_episode:
      oc.add(VideoClipObject(url=LATEST_URL % latest_episode, title='Latest Full Episode', thumb=R(thumb)))
  for show in feed_list:
    oc.add(DirectoryObject(key=Callback(GetVideoRSS, rss_url=show['link'], title1=title2, title2=show['title']), title=show['title'], thumb=R(thumb)))
  return oc
  
########################### Nighly News ############################################################
@route(PREFIX + '/nightlynews')
def Nightly_News():
  title2='Nightly News with Brian Williams'
  thumb=R('nightly_news.png')
  oc = FeedDirectory(feed_list=NIGHTLY_NEWS, title2='Nightly News with Brian Williams', thumb='nightly_news.png', latest_episode='MSNBC-NN-NETCAST-M4V')
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=NN_WEB, title1="Nightly News", title2="Web Only", thumb=thumb), title="Web Only", thumb=thumb))
  return oc
  
########################### END Nightly News END ###################################################
########################### Today Show ##############################################################
@route(PREFIX + '/today')
def Today():
  thumb = "today.png"
  title1= "Today Show"
  DirectoryObject.thumb = R(thumb)
  oc = ObjectContainer(title2=title1)
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_LATEST, title1=title1, title2="Latest Program", thumb=thumb,
    latest_episode='MSNBC-TDY-PODCAST-M4V'), title="Latest Program"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_NEWS, title1=title1, title2="News", thumb=thumb), title="News"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_CONCERT, title1=title1, title2="Concert Series", thumb=thumb), title="Concert Series"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_DIET, title1=title1, title2="Diet & Health", thumb=thumb), title="Diet & Health"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_ENTERTAINMENT, title1=title1, title2="Entertainment", thumb=thumb), title="Entertainment"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_FASHION, title1=title1, title2="Fashion", thumb=thumb), title="Fashion"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_WEDDINGS, title1=title1, title2="Relationships", thumb=thumb), title="Relationships"))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list=TS_SPECIAL, title1=title1, title2="Special Series", thumb=thumb), title="Special Series"))
  oc.extend(FeedDirectory(feed_list=TODAY_SHOW, title2=title1, thumb=thumb))
  oc.objects.sort(key = lambda obj: obj.title)
  return oc

########################### END Today Show END ###################################################
########################### All News ################################################################
@route(PREFIX + '/news')
def News():
  oc = ObjectContainer(title2='All News')
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_US, title2="U.S. News"), title="U.S. News")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_WORLD, title2="World News"), title="World News")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_BUSINESS, title2="Business"), title="Business")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_POLITICS, title2="Politics"), title="Politics")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_ENTERTAINMENT, title2="Entertainment"), title="Entertainment")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_HEALTH, title2="Health"), title="Health")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_SPORTS, title2="Sports"), title="Sports")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_TECH, title2="Tech & Science"), title="Tech & Science")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= NEWS_TRAVEL, title2="Travel"), title="Travel")))
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= WEATHER, title2="Weather"), title="Weather")))
  return oc

########################### END All News END #####################################################