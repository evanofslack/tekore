from typing import List
from dataclasses import dataclass

from spotipy.model.album.base import Album
from spotipy.model.member import Copyright
from spotipy.model.track import SimpleTrackPaging


@dataclass
class FullAlbum(Album):
    copyrights: List[Copyright]
    external_ids: dict
    genres: List[str]
    label: str
    popularity: int
    tracks: SimpleTrackPaging

    def __post_init__(self):
        super().__post_init__()
        self.copyrights = [Copyright(**c) for c in self.copyrights]
        self.tracks = SimpleTrackPaging(**self.tracks)
