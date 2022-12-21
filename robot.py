# Copyright 2022 Daniel Cruz
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import plotly.graph_objects as go

# Each object represents a poligon with its coordinates and color
# objects with multiple poligons will be animated
robotAnimation = [
    # Head
    {"fillColor": "#fce4d6", "frames": [
        [[10, 16], [10, 22], [16, 22], [16, 16]],
    ]},
    # Eyes
    {"fillColor": "#bdd7ee", "frames": [
        [[11.25, 19.35], [11.25, 20.5], [12.4, 20.5], [12.4, 19.35]],
    ]},
    {"fillColor": "#bdd7ee", "frames": [
        [[13.6, 19.35], [13.6, 20.5], [14.75, 20.5], [14.75, 19.35]],
    ]},
    # Nose
    {"fillColor": "#ffff00", "frames": [
        [[12.4, 18.2], [12.4, 18.5], [13.6, 18.5], [13.6, 18.2]],
    ]},
    # Mouth
    # (background)
    {"fillColor": "#000000", "frames": [
        [[11.2, 16.9], [11.2, 17.2], [14.8, 17.2], [14.8, 16.9]],
    ]},
    # grids
    {"fillColor": "#ffffff", "frames": [
        [[11.2, 17.2], [11.2, 17.5], [12.4, 17.5], [12.4, 17.2]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[12.4, 17.2], [12.4, 17.5], [13.6, 17.5], [13.6, 17.2]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[13.6, 17.2], [13.6, 17.5], [14.8, 17.5], [14.8, 17.2]],
    ]},
    #
    {"fillColor": "#ffffff", "frames": [
        [[11.2, 16.9], [11.2, 17.2], [12.4, 17.2], [12.4, 16.9]],
        [[11.2, 17.2], [11.2, 17.5], [12.4, 17.5], [12.4, 17.2]],
        [[11.2, 16.9], [11.2, 17.2], [12.4, 17.2], [12.4, 16.9]],
        [[11.2, 17.2], [11.2, 17.5], [12.4, 17.5], [12.4, 17.2]],
        [[11.2, 16.9], [11.2, 17.2], [12.4, 17.2], [12.4, 16.9]],
        [[11.2, 17.2], [11.2, 17.5], [12.4, 17.5], [12.4, 17.2]],
        [[11.2, 16.9], [11.2, 17.2], [12.4, 17.2], [12.4, 16.9]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[12.4, 16.9], [12.4, 17.2], [13.6, 17.2], [13.6, 16.9]],
        [[12.4, 17.2], [12.4, 17.5], [13.6, 17.5], [13.6, 17.2]],
        [[12.4, 16.9], [12.4, 17.2], [13.6, 17.2], [13.6, 16.9]],
        [[12.4, 17.2], [12.4, 17.5], [13.6, 17.5], [13.6, 17.2]],
        [[12.4, 16.9], [12.4, 17.2], [13.6, 17.2], [13.6, 16.9]],
        [[12.4, 17.2], [12.4, 17.5], [13.6, 17.5], [13.6, 17.2]],
        [[12.4, 16.9], [12.4, 17.2], [13.6, 17.2], [13.6, 16.9]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[13.6, 16.9], [13.6, 17.2], [14.8, 17.2], [14.8, 16.9]],
        [[13.6, 17.2], [13.6, 17.5], [14.8, 17.5], [14.8, 17.2]],
        [[13.6, 16.9], [13.6, 17.2], [14.8, 17.2], [14.8, 16.9]],
        [[13.6, 17.2], [13.6, 17.5], [14.8, 17.5], [14.8, 17.2]],
        [[13.6, 16.9], [13.6, 17.2], [14.8, 17.2], [14.8, 16.9]],
        [[13.6, 17.2], [13.6, 17.5], [14.8, 17.5], [14.8, 17.2]],
        [[13.6, 16.9], [13.6, 17.2], [14.8, 17.2], [14.8, 16.9]],
    ]},
    #
    {"fillColor": "#ffffff", "frames": [
        [[11.2, 16.6], [11.2, 16.9], [12.4, 16.9], [12.4, 16.6]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[12.4, 16.6], [12.4, 16.9], [13.6, 16.9], [13.6, 16.6]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[13.6, 16.6], [13.6, 16.9], [14.8, 16.9], [14.8, 16.6]],
    ]},
    # Antenas
    {"fillColor": "#a9d08e", "frames": [
        [[10, 22], [10, 23], [11.5, 23], [11.5, 22]],
        [[10.5, 22], [10.5, 23], [12, 23], [12, 22]],
        [[10, 22], [10, 23], [11.5, 23], [11.5, 22]],
        [[10.5, 22], [10.5, 23], [12, 23], [12, 22]],
        [[10, 22], [10, 23], [11.5, 23], [11.5, 22]],
        [[10.5, 22], [10.5, 23], [12, 23], [12, 22]],
        [[10, 22], [10, 23], [11.5, 23], [11.5, 22]],
    ]},
    {"fillColor": "#a9d08e", "frames": [
        [[14.5, 22], [14.5, 23], [16, 23], [16, 22]],
        [[14, 22], [14, 23], [15.5, 23], [15.5, 22]],
        [[14.5, 22], [14.5, 23], [16, 23], [16, 22]],
        [[14, 22], [14, 23], [15.5, 23], [15.5, 22]],
        [[14.5, 22], [14.5, 23], [16, 23], [16, 22]],
        [[14, 22], [14, 23], [15.5, 23], [15.5, 22]],
        [[14.5, 22], [14.5, 23], [16, 23], [16, 22]],
    ]},
    # Neck
    {"fillColor": "#fce4d6", "frames": [
        [[12.25, 14.5], [12.25, 16], [13.75, 16], [13.75, 14.5]],
    ]},
    # Body
    {"fillColor": "#e2efda", "frames": [
        [[10, 10], [10, 14.5], [16, 14.5], [16, 10]],
    ]},
    # Tie
    {"fillColor": "#548235", "frames": [
        [[12.25, 11], [12.25, 13.5], [13.75, 13.5], [13.75, 11]],
    ]},
    # Arms
    {"fillColor": "#ffffff", "frames": [
        [[8.5, 12.5], [8.5, 14.5], [10, 14.5], [10, 12.5]],
    ]},
    {"fillColor": "#fce4d6", "frames": [
        [[7, 12.5], [7, 13.75], [8.5, 13.75], [8.5, 12.5]],
        [[7, 13.25], [7, 14.5], [8.5, 14.5], [8.5, 13.25]],
        [[7, 12.5], [7, 13.75], [8.5, 13.75], [8.5, 12.5]],
        [[7, 13.25], [7, 14.5], [8.5, 14.5], [8.5, 13.25]],
        [[7, 12.5], [7, 13.75], [8.5, 13.75], [8.5, 12.5]],
        [[7, 13.25], [7, 14.5], [8.5, 14.5], [8.5, 13.25]],
    ]},
    {"fillColor": "#ffffff", "frames": [
        [[16, 12.5], [16, 14.5], [17.5, 14.5], [17.5, 12.5]],
    ]},
    {"fillColor": "#fce4d6", "frames": [
        [[17.5, 12.5], [17.5, 13.75], [19, 13.75], [19, 12.5]],
        [[17.5, 12.5], [17.5, 13.75], [19, 13.75], [19, 12.5]],
        [[17.5, 13.25], [17.5, 14.5], [19, 14.5], [19, 13.25]],
        [[17.5, 12.5], [17.5, 13.75], [19, 13.75], [19, 12.5]],
        [[17.5, 13.25], [17.5, 14.5], [19, 14.5], [19, 13.25]],
        [[17.5, 12.5], [17.5, 13.75], [19, 13.75], [19, 12.5]],
        [[17.5, 13.25], [17.5, 14.5], [19, 14.5], [19, 13.25]],
    ]},
    # Legs
    {"fillColor": "#e2efda", "frames": [
        [[10, 7.5], [10, 10], [11.5, 10], [11.5, 7.5]],
    ]},
    {"fillColor": "#e2efda", "frames": [
        [[14.5, 7.5], [14.5, 10], [16, 10], [16, 7.5]],
    ]},
    # Feet
    {"fillColor": "#806000", "frames": [
        [[8.5, 7], [8.5, 7.5], [11.5, 7.5], [11.5, 7]],
        [[9.5, 7], [9.5, 7.5], [12.5, 7.5], [12.5, 7]],
        [[8.5, 7], [8.5, 7.5], [11.5, 7.5], [11.5, 7]],
        [[9.5, 7], [9.5, 7.5], [12.5, 7.5], [12.5, 7]],
        [[8.5, 7], [8.5, 7.5], [11.5, 7.5], [11.5, 7]],
        [[9.5, 7], [9.5, 7.5], [12.5, 7.5], [12.5, 7]],
        [[8.5, 7], [8.5, 7.5], [11.5, 7.5], [11.5, 7]],
    ]},
    {"fillColor": "#806000", "frames": [
        [[14.5, 7], [14.5, 7.5], [17.5, 7.5], [17.5, 7]],
        [[13.5, 7], [13.5, 7.5], [16.5, 7.5], [16.5, 7]],
        [[14.5, 7], [14.5, 7.5], [17.5, 7.5], [17.5, 7]],
        [[13.5, 7], [13.5, 7.5], [16.5, 7.5], [16.5, 7]],
        [[14.5, 7], [14.5, 7.5], [17.5, 7.5], [17.5, 7]],
        [[13.5, 7], [13.5, 7.5], [16.5, 7.5], [16.5, 7]],
        [[14.5, 7], [14.5, 7.5], [17.5, 7.5], [17.5, 7]],
    ]},
]


def getNumberOfFrames(animationData):
    numberOfFrames = 0
    for animationElement in animationData:
        if numberOfFrames < len(animationElement["frames"]):
            numberOfFrames = len(animationElement["frames"])
    return numberOfFrames


def generateFrameDataForElement(frameNumber, frameElement):
    if (frameNumber > len(frameElement["frames"]) - 1):
        frameNumber = len(frameElement["frames"]) - 1

    frame = frameElement["frames"][frameNumber][:]
    # put the first element as the last one so the shape is closed
    frame.append(frame[0])
    return go.Scatter(
        x=[coordinate[0] for coordinate in frame], y=[coordinate[1] for coordinate in frame],
        mode="lines",
        fill="toself",
        line=dict(color="#000"),
        fillcolor=frameElement["fillColor"]
    )


def generateFrameData(frameNumber, animationData):
    return [generateFrameDataForElement(frameNumber, frameElement) for frameElement in animationData]


def generateFrame(frameNumber, imageData):
    return go.Frame(
        data=generateFrameData(frameNumber, imageData)
    )


fig = go.Figure(
    data=generateFrameData(0, robotAnimation),
    layout=go.Layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                     dict(
                         label="Play",
                         method="animate",
                         args=[None]
                     )
                ]
            )
        ]
    ),
    frames=[
        generateFrame(i, robotAnimation) for i in range(1, getNumberOfFrames(robotAnimation))
    ]
)

fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Set axes properties
fig.update_xaxes(range=[0, 25], showgrid=False, zeroline=False, visible=False)
fig.update_yaxes(range=[0, 25], showgrid=False, zeroline=False, visible=False)

fig.show()
