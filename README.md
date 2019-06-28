# str-to-json

a simple script that format JSON string in the clipboard and formatted it
prettier.

## Installation

Using pip

`pip install str-to-json`

## Usage

Copy a JSON string to your clipboard. Example:
`{"id": "uo-ca-en-CA-5729e0a833e541939d1da60a8a783e4d", "action": "delete"}`

run the script
`str-to-json`

Paste. It will turn your clipboard to
```
{
    "action": "delete",
    "id": "uo-ca-en-CA-5729e0a833e541939d1da60a8a783e4d"
}
```

