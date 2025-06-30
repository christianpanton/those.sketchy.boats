# those.sketchy.boats

Data used for sketchy.boats


## Description of the .imo format
The file represents IMO number of boat that need to be tagged for particular sketchiness.

Each file consists of a header prefixed with `#` followed by one IMO number per line.

Each IMO number/boat can have a comment, that follows immedately after the first whitespace (typically `\t`) character.

The header is used as description for the skechiness.

The sketchniess tag name is derived from the filename and folder.

Markdown is supported in both types of comments (boat and headers). In the boat comments, inclusion of a prefixed IMO number such as `IMO:1234567`, gets automatically converted to a link to that sketchy boat.

## Example
```
# This is a header, it can include **Markdown**
1234567 This boat is sketchy because reasons
8888888 This boat is linked to IMO:1234567
9999999 Here **Markdown** is supported as well!
```