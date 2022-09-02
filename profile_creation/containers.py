from dataclasses import dataclass
from enum import Enum

import geopandas as gpd
from shapely.geometry import LineString


class BeforeOrAfterFloodScenario(Enum):
    bf_2020 = "BF2020"
    af_2020 = "AF2020"


@dataclass(frozen=True)
class PathsForProfileCreation:
    path_to_raster: str
    path_to_gps_points: str
    path_to_water_mask: str


@dataclass(frozen=True)
class PointsPerProfile:
    gps_points: gpd.GeoDataFrame
    profile_line: LineString


@dataclass(frozen=True)
class ProjectedPointsPerProfileLine:
    projected_gps_points: gpd.GeoDataFrame
    profile_line: LineString


class OrderedProjectedGpsPointsPerProfileLine(ProjectedPointsPerProfileLine):
    pass
