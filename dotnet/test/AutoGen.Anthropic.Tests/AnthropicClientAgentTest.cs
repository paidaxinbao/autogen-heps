// Copyright (c) Microsoft Corporation. All rights reserved.
// AnthropicClientAgentTest.cs

using AutoGen.Anthropic.DTO;
using AutoGen.Anthropic.Extensions;
using AutoGen.Anthropic.Utils;
using AutoGen.Core;
using AutoGen.Tests;
using FluentAssertions;
using Xunit.Abstractions;

namespace AutoGen.Anthropic.Tests;

public class AnthropicClientAgentTest
{
    private readonly ITestOutputHelper _output;

    public AnthropicClientAgentTest(ITestOutputHelper output) => _output = output;

    [ApiKeyFact("ANTHROPIC_API_KEY")]
    public async Task AnthropicAgentChatCompletionTestAsync()
    {
        var client = new AnthropicClient(new HttpClient(), AnthropicConstants.Endpoint, AnthropicTestUtils.ApiKey);

        var agent = new AnthropicClientAgent(
            client,
            name: "AnthropicAgent",
            AnthropicConstants.Claude3Haiku).RegisterMessageConnector();

        var singleAgentTest = new SingleAgentTest(_output);
        await singleAgentTest.UpperCaseTestAsync(agent);
        await singleAgentTest.UpperCaseStreamingTestAsync(agent);
    }

    [ApiKeyFact("ANTHROPIC_API_KEY")]
    public async Task AnthropicAgentTestProcessImageAsync()
    {
        var client = new AnthropicClient(new HttpClient(), AnthropicConstants.Endpoint, AnthropicTestUtils.ApiKey);
        var agent = new AnthropicClientAgent(
            client,
            name: "AnthropicAgent",
            AnthropicConstants.Claude3Haiku).RegisterMessageConnector();

        var base64Image = await AnthropicTestUtils.Base64FromImageAsync("square.png");
        var imageMessage = new ChatMessage("user",
            [new ImageContent { Source = new ImageSource { MediaType = "image/png", Data = base64Image } }]);

        var messages = new IMessage[] { MessageEnvelope.Create(imageMessage) };

        // test streaming
        foreach (var message in messages)
        {
            var reply = agent.GenerateStreamingReplyAsync([message]);

            await foreach (var streamingMessage in reply)
            {
                streamingMessage.Should().BeOfType<TextMessageUpdate>();
                streamingMessage.As<TextMessageUpdate>().From.Should().Be(agent.Name);
            }
        }
    }
}
