import argparse
import sys
from google.cloud import videointelligence
import io
import json
import pytest

class something(object):
    # with pytest.raises(Exception) as excinfo:
    label_desc = []
    vid_pos_desc = []
    vid_con_desc = []
    shot_pos_desc = []
    shot_con_desc = []
    vid_results = {}
    shot_results = {}
    """Detect labels given a file path."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(sys.argv[1], 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(
        features=features, input_content=input_content)
    # print('\nProcessing video for label annotations:')

    result = operation.result(timeout=90)
    # print('\nFinished processing.')

    # Process video/segment level label annotations
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        desc = segment_label.entity.description
        # print('Video label description: {}'.format(
        #     segment_label.entity.description))
        # for category_entity in segment_label.category_entities:
        #     print('\tLabel category description: {}'.format(
        #         category_entity.description))
        vid_results[desc] = {}
        # data = vid_results[desc]
        for i, segment in enumerate(segment_label.segments):
            start_time = (segment.segment.start_time_offset.seconds +
                          segment.segment.start_time_offset.nanos / 1e9)
            end_time = (segment.segment.end_time_offset.seconds +
                        segment.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = segment.confidence
            vid_results[desc][positions] = confidence
            # vid_pos_desc.append(positions)
            # vid_con_desc.append(confidence)
        # print(vid_results)
        # input()
        # data = vid_results[desc]
        # data[]
        # data['positions'] = vid_pos_desc
    #     # data['confidence'] = vid_con_desc
    # print(vid_results)

    # print('\n')
    # Process shot level label annotations
    shot_labels = result.annotation_results[0].shot_label_annotations
    for i, shot_label in enumerate(shot_labels):
        desc = shot_label.entity.description
        # print('Shot label description: {}'.format(
        #     shot_label.entity.description))
        # for category_entity in shot_label.category_entities:
        #     print('\tLabel category description: {}'.format(
        #         category_entity.description))
        vid_results[desc] = {}
        # data = vid_results[desc]
        for i, shot in enumerate(shot_label.segments):
            start_time = (shot.segment.start_time_offset.seconds +
                          shot.segment.start_time_offset.nanos / 1e9)
            end_time = (shot.segment.end_time_offset.seconds +
                        shot.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = shot.confidence
            vid_results[desc][positions] = confidence
            # shot_con_desc.append(confidence)
            # shot_pos_desc.append(positions)
    print(json.dumps(vid_results))
    sys.stdout.flush()
        #     shot_results[desc] = {}
        #     data = shot_results[desc]
        #     data['positions'] = shot_pos_desc
        #     data['confidence'] = shot_con_desc
        #     print(shot_results)
        #     input('checl')
        # print(shot_results)

            

        # # Process frame level label annotations
        # frame_labels = result.annotation_results[0].frame_label_annotations
        # for i, frame_label in enumerate(frame_labels):
        #     print('Frame label description: {}'.format(
        #         frame_label.entity.description))
        #     for category_entity in frame_label.category_entities:
        #         print('\tLabel category description: {}'.format(
        #             category_entity.description))

        #     # Each frame_label_annotation has many frames,
        #     # here we print information only about the first frame.
        #     frame = frame_label.frames[0]
        #     time_offset = frame.time_offset.seconds + frame.time_offset.nanos / 1e9
        #     print('\tFirst frame time offset: {}s'.format(time_offset))
        #     print('\tFirst frame confidence: {}'.format(frame.confidence))
        #     print('\n')
