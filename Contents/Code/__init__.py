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
US_NEWS = [
  {'title'  :  'Latest Clips',      'link'  :  '21426262/device/rss'},  {'title'  :  'Crime & Courts',      'link'  :  '21427653/device/rss'},
  {'title'  :  'Education',         'link'  :  '23600346/device/rss'},  {'title'  :  'The Elkhart Project', 'link'  :  '29637267/device/rss'},
  {'title'  :  'Environment',       'link'  :  '21427657/device/rss'},  {'title'  :  'Faith"',              'link'  :  '23600340/device/rss'},
  {'title'  :  'Life"',             'link'  :  '21427662/device/rss'},  {'title'  :  'Military',            'link'  :  '21427669/device/rss'},
  {'title'  :  'Race & Ethnicity',  'link'  :  '21427673/device/rss'},  {'title'  :  'Security',            'link'  :  '21427678/device/rss'},
  {'title'  :  'Weird News',        'link'  :  '18424731/device/rss'}
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
  oc.add(DirectoryObject(key=Callback(FeedDirectory, feed_list= US_NEWS, title2="U.S. News"), title="U.S. News")))
  '''
  dir.Append(Function(DirectoryItem(N_World,          title="World news")))
  dir.Append(Function(DirectoryItem(N_Business,       title="Business")))
  dir.Append(Function(DirectoryItem(N_Politics,       title="Politics")))
  dir.Append(Function(DirectoryItem(N_Entertainment,  title="Entertainment")))
  dir.Append(Function(DirectoryItem(N_Health,         title="Health")))
  dir.Append(Function(DirectoryItem(N_Sports,         title="Sports")))
  dir.Append(Function(DirectoryItem(N_Tech,           title="Tech & Science")))
  dir.Append(Function(DirectoryItem(N_Travel,         title="Travel")))
  dir.Append(Function(DirectoryItem(N_Weather,        title="Weather")))
  '''
  return oc

@route(PREFIX + '/newsworld')
def N_World():
  dir = MediaContainer(title2='World News')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='21426473/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Americas"), name=MSNBC_URL + '21427766/device/rss', title2='Americas'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Africa"), name=MSNBC_URL + '21427760/device/rss', title2='Africs'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Asia-Pacific"), name=MSNBC_URL + '21427768/device/rss', title2='Asia-Pacific'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Conflict in Iraq"), name=MSNBC_URL + '21427754/device/rss', title2='Conflict in Iraq'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Europe"), name=MSNBC_URL + '21427850/device/rss', title2='Europe'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="South & Central Asia"), name=MSNBC_URL + '21427861/device/rss', title2='South & Central Asia'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Middle East & N. Africa"), name=MSNBC_URL + '21427857/device/rss', title2='Middle East & N. Africa'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Terrorism"), name=MSNBC_URL + '21427756/device/rss', title2='Terrorism'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Wonderful World"), name=MSNBC_URL + '21427651/device/rss', title2='Wonderful World'))
  return dir

@route(PREFIX + '/newsbusiness')
def N_Business():
  dir = MediaContainer(title2='Business')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='18424694/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Stock and Economy"), name=MSNBC_URL + '21427890/device/rss', title2='Stocks and Economy'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="U.S. Business"), name=MSNBC_URL + '21427903/device/rss', title2='U.S. Business'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Autos"), name=MSNBC_URL + '21427924/device/rss', title2='Autos'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Real Estate"), name=MSNBC_URL + '21427971/device/rss', title2='Real Estate'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Retail"), name=MSNBC_URL + '21427996/device/rss', title2='Retail'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Careers"), name=MSNBC_URL + '21427991/device/rss', title2='Careers'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Personal Finance"), name=MSNBC_URL + '21427918/device/rss', title2='Personal Finance'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Small Business"), name=MSNBC_URL + '21427920/device/rss', title2='Small Business'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Your Business"), name=MSNBC_URL + '18424833/device/rss', title2='Your Business'))
  return dir

@route(PREFIX + '/newspolitics')
def N_Politics():
  dir = MediaContainer(title2='Politics')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='18424734/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="The White House"), name=MSNBC_URL + '21427723/device/rss', title2='The White House'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Capitol Hill"), name=MSNBC_URL + '21427731/device/rss', title2='Capitol Hill'))
  dir.Append(Function(DirectoryItem(Morning_Joe,      title="Morning Joe", thumb=R('joe.png'))))
  dir.Append(Function(DirectoryItem(Hardball,         title="Hardball", thumb=R('hardball.jpeg'))))
  dir.Append(Function(DirectoryItem(Meet_The_Press,   title="Meet The Press", thumb=R('meet_the_press.png'))))
  return dir

@route(PREFIX + '/newsentertainment')
def N_Entertainment():
  dir = MediaContainer(title2='Entertainment')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='18424692/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Scoop", thumb=R('joe.png')), name=MSNBC_URL + '28184387/device/rss/vp/28159725', title2='Scoop'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Celebrities"), name=MSNBC_URL + '21428100/device/rss', title2='Celebrities'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Television"), name=MSNBC_URL + '21428108/device/rss', title2='Television'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Movies"), name=MSNBC_URL + '18424697/device/rss', title2='Movies'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Music"), name=MSNBC_URL + '21428116/device/rss', title2='Music'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Lifestyle"), name=MSNBC_URL + '21428119/device/rss', title2='Lifestyle'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Access Hollywood"), name=MSNBC_URL + '20418142/device/rss', title2='Access Hollywoody'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Keeping Tabs"), name=MSNBC_URL + '20498047/device/rss', title2='Keeping Tabs'))
  return dir

@route(PREFIX + '/newshealth')
def N_Health():
  dir = MediaContainer(title2='Health')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='21427299/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Diet & Nutrition"), name=MSNBC_URL + '21428136/device/rss', title2='Diet & Nutrition'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Women's Health"), name=MSNBC_URL + '21428143/device/rss', title2="Women's Health"))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Men's Health"), name=MSNBC_URL + '21428151/device/rss', title2="Men's Health"))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Kids & Parenting"), name=MSNBC_URL + '21428155/device/rss', title2='Kids & Parenting'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Health Care"), name=MSNBC_URL + '30018753/device/rss', title2='Health Care'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Food Safety"), name=MSNBC_URL + '30018791/device/rss', title2='Food Safety'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Sexual Health"), name=MSNBC_URL + '21428170/device/rss', title2='Sexual Health'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Pet Health"), name=MSNBC_URL + '21428208/device/rss', title2='Pet Health'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Fitness"), name=MSNBC_URL + '21428178/device/rss', title2='Fitness'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Heart Health"), name=MSNBC_URL + '21428183/device/rss', title2='Heart Health'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Mental Health"), name=MSNBC_URL + '21428162/device/rss', title2='Mental Health'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Cancer"), name=MSNBC_URL + '21428191/device/rss', title2='Cancer'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Aging"), name=MSNBC_URL + '21428203/device/rss', title2='Aging'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Skin & Beauty"), name=MSNBC_URL + '21480182/device/rss', title2='Skin & Beauty'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Animal Tracks"), name=MSNBC_URL + '18424682/device/rss', title2='Animal Tracks'))
  return dir

@route(PREFIX + '/newssports')
def N_Sports():
  dir = MediaContainer(title2='Sports')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Sports"), name='http://pheedo.msnbc.msn.com/id/21426493/device/rss/', title2='Latest Sports'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NFL"), name='http://nbcsports.msnbc.com/id/21428022/device/rss', title2='NFL'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Baseball"), name='http://nbcsports.msnbc.com/id/21428015/device/rss', title2='Baseball'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NCAA Hoops"), name='http://nbcsports.msnbc.com/id/21428068/device/rss', title2='NCAA Hoops'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NBA"), name='http://nbcsports.msnbc.com/id/21428039/device/rss', title2='NBA'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Golf"), name='http://nbcsports.msnbc.com/id/21428026/device/rss', title2='Golf'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NHL"), name='http://nbcsports.msnbc.com/id/21428025/device/rss', title2='NHL'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="MMA"), name='http://nbcsports.msnbc.com/id/21428080/device/rss', title2='MMA'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NCAA Football"), name='http://nbcsports.msnbc.com/id/21428047/device/rss', title2='NCAA Football'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Horse Racing"), name='http://nbcsports.msnbc.com/id/21428075/device/rss', title2='Horse Racing'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="NASCAR/Motors"), name='http://nbcsports.msnbc.com/id/22114938/device/rss', title2='NASCAR/Motors'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Tennis"), name='http://nbcsports.msnbc.com/id/21428033/device/rss', title2='Tennis'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Sports Oddities"), name='http://nbcsports.msnbc.com/id/23017283/device/rss', title2='Sports Oddities'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Mad Dog Minute"), name='http://nbcsports.msnbc.com/id/23017809/device/rss', title2='Mad Dog Minute'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Matty Blake"), name='http://nbcsports.msnbc.com/id/23258082/device/rss', title2='Matty Blake'))
  return dir

@route(PREFIX + '/newstech')
def N_Tech():
  dir = MediaContainer(title2='Tech')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='18424747/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Space"), name=MSNBC_URL + '18424741/device/rss', title2='Space'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Science"), name=MSNBC_URL + '21428316/device/rss', title2='Science'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Technology"), name=MSNBC_URL + '21428240/device/rss', title2='Technology'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Games"), name=MSNBC_URL + '26560891/device/rss', title2='Games'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Red Tape Chronicals"), name=MSNBC_URL + '28780760/device/rss', title2='Red Tape Chronicals'))
  return dir

@route(PREFIX + '/newstravel')
def N_Travel():
  dir = MediaContainer(title2='Travel')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name='21427411/device/rss/', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Travel Tips"), name=MSNBC_URL + '26560980/device/rss', title2='Travel Tips'))
  return dir

@route(PREFIX + '/newsweather')
def N_Weather():
  dir = MediaContainer(title2='Weather')
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Latest Clips"), name=MSNBC_URL + '25198763/device/rss', title2='Latest Clips'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="National Forecasts"), name=MSNBC_URL + '30331543/device/rss', title2='National Forecasts'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Regional Forecasts"), name=MSNBC_URL + '30331544/device/rss', title2='Regional Forecasts'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Top Local Forecasts"), name=MSNBC_URL + '30331545/device/rss', title2='Top Local Forecasts'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Vacation Forecasts"), name=MSNBC_URL + '30331546/device/rss', title2='Vacation Forecasts'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Forecast Earth"), name=MSNBC_URL + '30331549/device/rss', title2='Forecast Earth'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Epic Conditions"), name=MSNBC_URL + '30332550/device/rss', title2='Epic Conditions'))
  dir.Append(Function(DirectoryItem(GetVideosRSS,     title="Weather Changed History"), name=MSNBC_URL + '30331551/device/rss', title2='Weather Changed History'))
  return dir

########################### END All News END #####################################################