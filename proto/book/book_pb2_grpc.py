# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto.book import book_pb2 as proto_dot_book_dot_book__pb2
from proto.user import user_pb2 as proto_dot_user_dot_user__pb2


class BookControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UserBookList = channel.unary_unary(
                '/book.BookController/UserBookList',
                request_serializer=proto_dot_user_dot_user__pb2.User.SerializeToString,
                response_deserializer=proto_dot_book_dot_book__pb2.UserBooksResponse.FromString,
                )
        self.List = channel.unary_stream(
                '/book.BookController/List',
                request_serializer=proto_dot_book_dot_book__pb2.BookListRequest.SerializeToString,
                response_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                )
        self.Create = channel.unary_unary(
                '/book.BookController/Create',
                request_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
                response_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/book.BookController/Retrieve',
                request_serializer=proto_dot_book_dot_book__pb2.BookRetrieveRequest.SerializeToString,
                response_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                )
        self.Update = channel.unary_unary(
                '/book.BookController/Update',
                request_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
                response_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/book.BookController/Destroy',
                request_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class BookControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UserBookList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UserBookList': grpc.unary_unary_rpc_method_handler(
                    servicer.UserBookList,
                    request_deserializer=proto_dot_user_dot_user__pb2.User.FromString,
                    response_serializer=proto_dot_book_dot_book__pb2.UserBooksResponse.SerializeToString,
            ),
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=proto_dot_book_dot_book__pb2.BookListRequest.FromString,
                    response_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                    response_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=proto_dot_book_dot_book__pb2.BookRetrieveRequest.FromString,
                    response_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                    response_serializer=proto_dot_book_dot_book__pb2.Book.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=proto_dot_book_dot_book__pb2.Book.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'book.BookController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UserBookList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookController/UserBookList',
            proto_dot_user_dot_user__pb2.User.SerializeToString,
            proto_dot_book_dot_book__pb2.UserBooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/book.BookController/List',
            proto_dot_book_dot_book__pb2.BookListRequest.SerializeToString,
            proto_dot_book_dot_book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookController/Create',
            proto_dot_book_dot_book__pb2.Book.SerializeToString,
            proto_dot_book_dot_book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookController/Retrieve',
            proto_dot_book_dot_book__pb2.BookRetrieveRequest.SerializeToString,
            proto_dot_book_dot_book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookController/Update',
            proto_dot_book_dot_book__pb2.Book.SerializeToString,
            proto_dot_book_dot_book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/book.BookController/Destroy',
            proto_dot_book_dot_book__pb2.Book.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
