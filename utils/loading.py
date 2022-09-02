import geopandas as gpd


def check_that_all_geometries_are_set(loaded_data: gpd.GeoDataFrame) -> bool:
    return all(geom is not None for geom in loaded_data.geometry)


def check_that_all_geometries_are_the_same(loaded_data: gpd.GeoDataFrame) -> bool:
    first_geom = loaded_data.geometry[0]
    return all(isinstance(geom, first_geom.__class__) is not None for geom in loaded_data.geometry)


def load_data_with_crs_2056(path_to_data: str) -> gpd.geodataframe:
    loaded_data = gpd.read_file(path_to_data)
    if loaded_data.crs is None:
        loaded_data.crs = 2056
    assert check_that_all_geometries_are_set(loaded_data)
    assert check_that_all_geometries_are_the_same(loaded_data)
    assert loaded_data.crs == 2056
    return loaded_data
