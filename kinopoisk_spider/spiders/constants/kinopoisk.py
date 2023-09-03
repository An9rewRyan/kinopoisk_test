# -*- coding:utf-8 -*-

# spider constants template
# m.eremenko@brandquad.ru
# 03.09.2023
#
# source: kinopoisk
#

GRAPHQL_HEADERS = {
    "Accept-Language": "ru,en;q=0.9",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Preferred-Language": "ru",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Service-Id": "25",
    "Sec-Ch-Ua-Platform": "",
    "Origin": "https://www.kinopoisk.ru",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.kinopoisk.ru/",
    "Accept-Encoding": "gzip, deflate",
}
KINOPOISK_URL = "https://graphql.kinopoisk.ru/graphql/?operationName=MovieDesktopListPage"

GRAPHQL_BODY = {"operationName": "MovieDesktopListPage",
                "variables": {"slug": "top_1000", "platform": "DESKTOP", "regionId": 10995, "withUserData": False,
                              "supportedFilterTypes": ["BOOLEAN", "SINGLE_SELECT"],
                              "filters": {"booleanFilterValues": [], "intRangeFilterValues": [],
                                          "singleSelectFilterValues": [],
                                          "multiSelectFilterValues": [], "realRangeFilterValues": []},
                              "singleSelectFiltersLimit": 250,
                              "singleSelectFiltersOffset": 0, "moviesLimit": 50, "moviesOffset": 0,
                              "moviesOrder": "POSITION_ASC",
                              "supportedItemTypes": ["COMING_SOON_MOVIE_LIST_ITEM", "MOVIE_LIST_ITEM",
                                                     "TOP_MOVIE_LIST_ITEM",
                                                     "POPULAR_MOVIE_LIST_ITEM", "MOST_PROFITABLE_MOVIE_LIST_ITEM",
                                                     "MOST_EXPENSIVE_MOVIE_LIST_ITEM", "BOX_OFFICE_MOVIE_LIST_ITEM",
                                                     "OFFLINE_AUDIENCE_MOVIE_LIST_ITEM",
                                                     "RECOMMENDATION_MOVIE_LIST_ITEM"]},
                "query": "query MovieDesktopListPage($slug: String!, $platform: WebClientPlatform!, $withUserData: Boolean!, $regionId: Int!, $supportedFilterTypes: [FilterType]!, $filters: FilterValuesInput, $singleSelectFiltersLimit: Int!, $singleSelectFiltersOffset: Int!, $moviesLimit: Int, $moviesOffset: Int, $moviesOrder: MovieListItemOrderBy, $supportedItemTypes: [MovieListItemType]) { movieListBySlug(slug: $slug, supportedFilterTypes: $supportedFilterTypes, filters: $filters) { id name description cover { avatarsUrl __typename } ...MovieListCompositeName ...MovieListAvailableFilters ...MovieList ...DescriptionLink __typename } webPage(platform: $platform) { kpMovieListPage(movieListSlug: $slug) { htmlMeta { ...OgImage __typename } footer { ...FooterConfigData __typename } featuring { ...MovieListFeaturingData __typename } __typename } __typename } } fragment MovieListCompositeName on MovieListMeta { compositeName { parts { ... on FilterReferencedMovieListNamePart { filterValue { ... on SingleSelectFilterValue { filterId __typename } __typename } name __typename } ... on StaticMovieListNamePart { name __typename } __typename } __typename } __typename } fragment MovieListAvailableFilters on MovieListMeta { availableFilters { items { ... on BooleanFilter { ...ToggleFilter __typename } ... on SingleSelectFilter { ...SingleSelectFilters __typename } __typename } __typename } __typename } fragment ToggleFilter on BooleanFilter { id enabled name { russian __typename } __typename } fragment SingleSelectFilters on SingleSelectFilter { id name { russian __typename } hint { russian __typename } values(offset: $singleSelectFiltersOffset, limit: $singleSelectFiltersLimit) { items { name { russian __typename } selectable value __typename } __typename } __typename } fragment MovieList on MovieListMeta { movies(limit: $moviesLimit, offset: $moviesOffset, orderBy: $moviesOrder, supportedItemTypes: $supportedItemTypes) { total items { movie { id contentId title { russian original __typename } poster { avatarsUrl fallbackUrl __typename } countries { id name __typename } genres { id name __typename } cast: members(role: [ACTOR], limit: 3) { items { details person { name originalName __typename } __typename } __typename } directors: members(role: [DIRECTOR], limit: 1) { items { details person { name originalName __typename } __typename } __typename } url rating { kinopoisk { isActive count value __typename } expectation { isActive count value __typename } __typename } mainTrailer { id isEmbedded __typename } viewOption { buttonText originalButtonText promotionIcons { avatarsUrl fallbackUrl __typename } isAvailableOnline: isWatchable(filter: {anyDevice: false, anyRegion: false}) purchasabilityStatus type rightholderLogoUrlForPoster availabilityAnnounce { availabilityDate type groupPeriodType announcePromise __typename } __typename } isTicketsAvailable(regionId: $regionId) ... on Film { productionYear duration isShortFilm top250 __typename } ... on TvSeries { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on MiniSeries { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on TvShow { releaseYears { start end __typename } seriesDuration totalDuration top250 __typename } ... on Video { productionYear duration isShortFilm __typename } ...MovieListUserData @include(if: $withUserData) __typename } ... on TopMovieListItem { position positionDiff rate votes __typename } ... on MostProfitableMovieListItem { boxOffice { amount __typename } budget { amount __typename } ratio __typename } ... on MostExpensiveMovieListItem { budget { amount __typename } __typename } ... on OfflineAudienceMovieListItem { viewers __typename } ... on PopularMovieListItem { positionDiff __typename } ... on BoxOfficeMovieListItem { boxOffice { amount __typename } __typename } ... on RecommendationMovieListItem { __typename } ... on ComingSoonMovieListItem { releaseDate { date accuracy __typename } __typename } __typename } __typename } __typename } fragment MovieListUserData on Movie { userData { folders { id name public __typename } watchStatuses { notInterested { value __typename } watched { value __typename } __typename } voting { value votedAt __typename } __typename } __typename } fragment DescriptionLink on MovieListMeta { descriptionLink { title url __typename } __typename } fragment OgImage on HtmlMeta { openGraph { image { avatarsUrl __typename } __typename } __typename } fragment FooterConfigData on FooterConfiguration { socialNetworkLinks { icon { avatarsUrl __typename } url title __typename } appMarketLinks { icon { avatarsUrl __typename } url title __typename } links { title url __typename } __typename } fragment MovieListFeaturingData on MovieListFeaturing { items { title url __typename } __typename } "}
