# Mars-Themed Robot Map Design

## Overview

The robot course map is designed to immerse learners in a Martian environment, utilizing **black roads** for line sensor navigation and **distinct color marks** for scientific zones. The map measures 1x1.5 meters, has a continuous black road forming a circuit around the perimeter, and includes specific zones modeled on Mars features for various tasks. The surface should feature reddish, sandy, or rocky textures and patterns to evoke the look of Mars[1].

## Map Layout and Zone Placement

### General Structure

- **Black Line Road**: A bold, continuous black line (4-6cm wide) defines the main circuit, running in a loop near the edges of the map (about 10-15cm from the edge), allowing full traversal and line-following around the entire field.
- **Martian Surface Texture**: Filling the space inside the track, use Mars-like coloring (reds, browns, oranges) for thematic immersion.
- **Zone Marking**: Each zone contains either a color patch (colored paper or tape) or a unique symbol, integrating with learning objectives.

### Zone Suggestions and Locations

| Zone Name      | Suggested Placement        | Description & Task Ideas                         | Color/Features             |
|:-------------- |:--------------------------|:------------------------------------------------|:---------------------------|
| Garage (Base)  | Bottom-left corner         | Start/finish area, for docking, charging, system check. Task: automatic "garage parking".| Blue or silver color patch |
| Crater         | Top-center                 | Navigation challenge: crater "hazard" avoidance or scanning. Task: go around crater without crossing. | Circular sandy/yellow patch|
| Sample Depot   | Bottom-right corner        | Place for "collecting" or "delivering" simulated Martian rock samples. Task: stop to simulate pick/drop. | Red/orange patch           |
| Research Lab   | Center                     | Zone for data upload/download (e.g. file I/O tasks), simulate a base station. | Green patch or marked area |
| Water Ice Patch| Top-right                  | Simulate discovery of water ice, requiring special action (slower movement, color detection). Task: slow down, log presence. | White/light blue area      |
| Rock Field     | Left-center                | Obstacle/slow zone with rougher texture or simulated "rocks" (e.g., small bumps), practice speed/steering controllers. | Area with brown/grey stones|
| Solar Panel Array | Top-left                | Perform "alignment" tasks: orient the robot precisely here (e.g., with an LED sensor). Task: align and stop. | Yellow patch or symbol     |

## Map Layout Example

```
+--------------------------------------------------+
|   [Solar Panel]    [Crater]       [Water Ice]    |
|       (Y)       (Yellow patch)  (White patch)    |
|        |              |               |          |
| [Rock Field]                      [Research Lab] |
|  (grey/brown)            (Green/centered circle) |
|        |                                  |      |
|   [Garage]                       [Sample Depot]  |
|   (Blue patch)                (Red/Orange patch) |
+--------------------------------------------------+
```

- **Main black road** follows the rectangle boundary, allowing each zone to be adjacent or connected to the track for easy robot access.
- **Curves or short spurs** from the main road can lead into zones (for precision tasks).
- **Color marks/symbols** inside zones for sensor-triggered actions.

## How Zones Support Lessons

**Garage (Base)**
- Starting and docking routines
- Automated parking, "wake-up" and system diagnostic tests

**Crater**
- Line following with avoidance (divert off/on path)
- Simulated hazard mapping

**Sample Depot**
- Pick-up or drop-off actions with precise stopping
- Task: use line/color sensor to trigger "sample" routines

**Research Lab**
- File/task simulation (write/read action)
- Communication or data processing task

**Water Ice Patch**
- Color sensor-based detection
- Modulate speed or movement based on zone color

**Rock Field**
- Terrain-based challenges (obstacle avoidance, speed control)
- Controller tuning for uneven "Martian" terrain

**Solar Panel Array**
- Precise stopping & orientation
- Task: activate LEDs, perform heading alignment

## Zone and Task Mapping Table

| Zone              | Key Lesson Applications                    |
|-------------------|--------------------------------------------|
| Garage            | Start/stop routines, docking, diagnostics  |
| Crater            | Obstacle navigation, hazard mapping        |
| Sample Depot      | Pick/drop tasks, position accuracy         |
| Research Lab      | File I/O, data operations, stopping        |
| Water Ice Patch   | Color detection, speed modulation          |
| Rock Field        | Obstacle avoidance, controller testing     |
| Solar Panel Array | Alignment, sensor calibration, LED control |

This map structure delivers a visually representative Mars surface while supporting a progressive, zone-based learning path for robot line following, color/sensor challenges, and advanced navigation tasks[1][2].

[1] https://wseas.com/journals/ew/2021/engw2021-013.pdf
[2] https://www.azorobotics.com/Article.aspx?ArticleID=61
[3] https://tabletopwhale.com/2016/02/27/here-there-be-robots.html
[4] https://vbn.aau.dk/ws/files/536077322/ROB10_MR_FAME_Report_3.pdf
[5] https://www-robotics.jpl.nasa.gov/media/documents/HelmickAero07tanav.pdf
[6] https://www.youtube.com/watch?v=FNjS6H-i1dA
[7] https://www-robotics.jpl.nasa.gov/media/documents/MER_Operations_with_SAP.pdf
[8] https://arxiv.org/html/2406.16713v4
[9] https://dspace.cuni.cz/bitstream/handle/20.500.11956/83769/BPTX_2015_1_11320_0_410161_0_174125.pdf?sequence=1&isAllowed=y
[10] https://www.ri.cmu.edu/pub_files/pub4/tompkins_paul_2005_1/tompkins_paul_2005_1.pdf
[11] https://www.reddit.com/r/geoguessr/comments/lwa9wr/map_of_european_road_curve_chevron_signs/
[12] https://www.sciencedirect.com/science/article/pii/S1877050923014199/pdf?md5=6b6882f25468dbd7862134ca22a5025c&pid=1-s2.0-S1877050923014199-main.pdf
[13] https://www.jpl.nasa.gov/edu/resources/collection/mission-to-mars-student-challenge/education-plan-design-your-spacecraft/
[14] https://warrobots.fandom.com/wiki/Mars
[15] https://arxiv.org/html/2311.08244v2
[16] https://www.mdpi.com/2072-4292/14/4/1027
[17] https://www.ri.cmu.edu/pub_files/pub1/ollis_mark_1997_1/ollis_mark_1997_1.pdf
[18] https://www-robotics.jpl.nasa.gov/media/documents/IEEEAC03-backes.pdf
[19] https://www.gov.uk/government/publications/know-your-traffic-signs/direction-signs-on-all-purpose-roads
[20] https://firstmonday.org/ojs/index.php/fm/article/view/4871/3812