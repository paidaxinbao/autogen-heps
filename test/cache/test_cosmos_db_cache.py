#!/usr/bin/env python3 -m pytest

import pickle
import unittest
from unittest.mock import MagicMock, patch

import pytest

try:
    from autogen.cache.cosmos_db_cache import CosmosDBCache

    skip_cosmos_tests = False
except ImportError:
    skip_cosmos_tests = True


class TestCosmosDBCache(unittest.TestCase):
    def setUp(self):
        self.seed = "test_seed"
        self.client = MagicMock()
        self.database_id = "test_database"
        self.container_id = "test_container"
        self.container_client_mock = MagicMock()
        self.client.get_database_client().get_container_client.return_value = self.container_client_mock
        self.value = "value"
        self.serialized_value = pickle.dumps(self.value)
        self.container_client_mock.read_item.return_value = {"data": self.serialized_value}

        # Create a configuration dictionary for CosmosDBCache
        self.cosmosdb_config = {
            "client": self.client,
            "database_id": self.database_id,
            "container_id": self.container_id,
        }

    @pytest.mark.skipif(skip_cosmos_tests, reason="Cosmos DB SDK not installed")
    def test_init(self):
        cache = CosmosDBCache(self.seed, self.cosmosdb_config)
        self.assertEqual(cache.seed, self.seed)
        self.assertEqual(cache.client, self.client)

    @pytest.mark.skipif(skip_cosmos_tests, reason="Cosmos DB SDK not installed")
    def test_get(self):
        key = "key"
        cache = CosmosDBCache(self.seed, self.cosmosdb_config)
        result = cache.get(key)
        self.assertEqual(result, self.value)
        self.container_client_mock.read_item.assert_called_with(item=key, partition_key=str(self.seed))

        self.container_client_mock.read_item.side_effect = Exception("not found")
        self.assertIsNone(cache.get(key, default=None))

    @pytest.mark.skipif(skip_cosmos_tests, reason="Cosmos DB SDK not installed")
    def test_set(self):
        key = "key"
        value = "value"
        cache = CosmosDBCache(self.seed, self.cosmosdb_config)
        cache.set(key, value)
        self.container_client_mock.upsert_item.assert_called_with(
            {"id": key, "partitionKey": str(self.seed), "data": self.serialized_value}
        )

    @pytest.mark.skipif(skip_cosmos_tests, reason="Cosmos DB SDK not installed")
    def test_context_manager(self):
        with CosmosDBCache(self.seed, self.cosmosdb_config) as cache:
            self.assertIsInstance(cache, CosmosDBCache)


if __name__ == "__main__":
    unittest.main()