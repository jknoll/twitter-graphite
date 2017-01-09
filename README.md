graphite-twitter
==

Sends a follower count to graphite.

    len(api.GetMentions())
    len(api.GetRetweetsOfMe())
    len(api.GetFavorites())
    len(api.GetFriends())

Other API endpoints for future reference and inclusion:

    pp([item for item in dir(api) if 'Get' in item])
    ['GetBlocks',
     'GetBlocksIDs',
     'GetBlocksIDsPaged',
     'GetBlocksPaged',
     'GetDirectMessages',
     'GetFavorites',
     'GetFollowerIDs',
     'GetFollowerIDsPaged',
     'GetFollowers',
     'GetFollowersPaged',
     'GetFriendIDs',
     'GetFriendIDsPaged',
     'GetFriends',
     'GetFriendsPaged',
     'GetHelpConfiguration',
     'GetHomeTimeline',
     'GetListMembers',
     'GetListMembersPaged',
     'GetListTimeline',
     'GetLists',
     'GetListsList',
     'GetListsPaged',
     'GetMemberships',
     'GetMentions',
     'GetMutes',
     'GetMutesIDs',
     'GetMutesIDsPaged',
     'GetMutesPaged',
     'GetReplies',
     'GetRetweeters',
     'GetRetweets',
     'GetRetweetsOfMe',
     'GetSearch',
     'GetSentDirectMessages',
     'GetShortUrlLength',
     'GetStatus',
     'GetStatusOembed',
     'GetStreamFilter',
     'GetStreamSample',
     'GetSubscriptions',
     'GetTrendsCurrent',
     'GetTrendsWoeid',
     'GetUser',
     'GetUserRetweets',
     'GetUserStream',
     'GetUserSuggestion',
     'GetUserSuggestionCategories',
     'GetUserTimeline',
     'GetUsersSearch',
     '_GetBlocksMutesPaged',
     '_GetFriendFollowerIDs',
     '_GetFriendsFollowers',
     '_GetFriendsFollowersPaged',
     '_GetIDsPaged']
