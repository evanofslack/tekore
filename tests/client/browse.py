from ._cred import TestCaseWithCredentials
from spotipy.client import SpotifyBrowse


class TestSpotifyArtist(TestCaseWithCredentials):
    category_id = 'pop'
    artist_ids = ['2SRIVGDkdqQnrQdaXxDkJt', '2aaLAng2L2aWD2FClzwiep']

    def setUp(self):
        self.client = SpotifyBrowse(self.app_token)

    def test_featured_playlists_with_country(self):
        msg, playlists = self.client.featured_playlists(country='US')
        self.assertTrue(playlists.total > 0)

    def test_featured_playlists_no_country(self):
        msg, playlists = self.client.featured_playlists()
        self.assertTrue(playlists.total > 0)

    def test_new_releases_with_country(self):
        albums = self.client.new_releases(country='US')
        self.assertTrue(albums.total > 0)

    def test_new_releases_no_country(self):
        albums = self.client.new_releases()
        self.assertTrue(albums.total > 0)

    def test_categories_with_country(self):
        cat = self.client.categories(country='US')
        self.assertTrue(cat.total > 0)

    def test_categories_no_country(self):
        cat = self.client.categories()
        self.assertTrue(cat.total > 0)

    def test_category_with_country(self):
        cat = self.client.category(self.category_id, country='US')
        self.assertEqual(cat.id, self.category_id)

    def test_category_no_country(self):
        cat = self.client.category(self.category_id)
        self.assertEqual(cat.id, self.category_id)

    def test_category_playlists_with_country(self):
        playlists = self.client.category_playlists(self.category_id, country='US')
        self.assertTrue(playlists.total > 0)

    def test_category_playlists_no_country(self):
        playlists = self.client.category_playlists(self.category_id)
        self.assertTrue(playlists.total > 0)

    def test_recommendations_with_market(self):
        rec = self.client.recommendations(
            artist_ids=self.artist_ids,
            market='US'
        )
        self.assertTrue(len(rec.tracks) > 0)

    def test_recommendations_no_market(self):
        rec = self.client.recommendations(
            artist_ids=self.artist_ids,
            market=None
        )
        self.assertTrue(len(rec.tracks) > 0)

    def test_recommendations_target_attribute(self):
        rec = self.client.recommendations(
            artist_ids=self.artist_ids,
            market='US',
            target_valence=50
        )
        self.assertTrue(len(rec.tracks) > 0)

    def test_recommendations_invalid_attribute_raises(self):
        with self.assertRaises(ValueError):
            self.client.recommendations(
                artist_ids=self.artist_ids,
                market='US',
                maxbogus=50
            )

    def test_recommendations_invalid_attribute_name_raises(self):
        with self.assertRaises(ValueError):
            self.client.recommendations(
                artist_ids=self.artist_ids,
                market='US',
                max_bogus=50
            )

    def test_recommendations_invalid_attribute_prefix_raises(self):
        with self.assertRaises(ValueError):
            self.client.recommendations(
                artist_ids=self.artist_ids,
                market='US',
                bogus_valence=50
            )

    def test_recommendation_genre_seeds(self):
        seeds = self.client.recommendation_genre_seeds()
        self.assertTrue(len(seeds) > 0)