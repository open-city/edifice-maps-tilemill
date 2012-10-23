Edifice Maps TileMill Projects
===================

[TileMill](http://mapbox.com/tilemill/) projects + geodata for [Edifice Maps](https://github.com/open-city/edifice-maps), a series of maps exploring Chicago's built environment.


# Building areas

`building_areas/`

Map of [every building in Chicago](edifice.opencityapps.org), colored by its footprint area. 

`data/buildings_tilemill.csv` is the base data, but you'll need to join in addresses and land use, or email us for a dump of the final database.


# Construction Spending

`construction_spending/`

Map of total construction spending by census block group.

`census_block_groups.sql` has basic data on census block groups geometry. To find construction spending per block group, you need to aggregate construction permits in `new_const_permits/new_const_permits.sql`.


# Building demolitions

`new_demo_permits/`

Map of every building demolished since 2006. 

`new_demo_permits.sql` is the data. To style it, load it into PostgreSQL + PostGIS, and connect to it with TileMill.


# Building violations

`new_violations/`

Every building violation issued by the City of Chicago since 2006. `new_violations.sql` has the data.


# Building Renovations

`new_renov_permits/`

Data for every building rehabbed since 2006. Each building has count of renovation permits issued and details about its most recent renovation.

`new_renov_permits.sql` has the data. Never made a map out of it. That's why there's no .mss or .mml files.