# Abstraction: The Developer's Way of Thinking

Before diving into "developer stuff" like programming languages, it is important to first understand the idea of **abstraction**, which is a fundamental concept underlying **all** software systems, hardware architectures, and essentially, all complicated things.

Abstraction helps to manage the complexity of real world systems, to break down complex systems into simpler components and to allow both the creator and non-creators something to quickly understand "what this thing is". Abstraction is found in almost every aspect in the modern world, from software applications to hardware and even "non-technical" industries such as animated films. However, it is especially important to developers as they deal with and use this concept every day. Essentially, abstraction should be the second instinct of all developers.

## What is "Abstraction"?

Generally speaking, "to abstract" roughly means "**to define what something is to someone, disregarding all irrelevant information**".

According to the definition above, there are two important questions to ask when abstracting something:

1. **What is this thing?**
2. **What information are relevant? What information are not? I.e., What does that "someone" need to know about?**

Notice that both of these questions are dependent to the "target audience" of the abstraction, i.e., the person (or the system) that will use the abstraction. If your audience changes, the "thing" might look different, relevant information might become irrelevant, and vice versa.

Abstraction is not meant for other people only; sometimes (actually most of the time), the target audience will be yourself who is designing and implementing the thing to be abstracted.

Although I gave a definition above, abstraction itself is an "abstract" idea which is very hard to define clearly, and there is no broadly-accepted definition. So, I will use an example to illustrate what abstraction really means.

## An Example of Abstraction

| ![abstracted-car](res/car-abstraction.png) | ![concrete-car](res/car-mechanics.png) |
| -- | -- |

When you're in a morning rush and you see a car, what first comes to your mind? Is it "I can drive this thing around", or chasis, engine, tires and fuel tanks?

I believe most people's view would be the former. Of course, the latter view is also important, but it is **irrelevant** to you at the moment: you're in a rush, so all that matters to you is that you can drive a car to get to your workplace fast.

Believe it or not, you have already used abstraction in the example above. Let's break it down a little:

- Target of abstraction: The car.
- Target audience: You.
- What is this thing: Something you can use to drive around and get to anywhere fast.
- Relevant information: You can drive this thing around. It's fast.
- Irrelevant information: It's made up of an engine, a fuel tank, a chasis, etc. It's 4.6 meters long and 1.6 meters tall, with a peak power output of 140 hp. Stuff like that.

The explanation above should be easy to understand: the target audience is you, and the only thing you need to know is that you can drive a car around, so that's the abstraction.

For workers at a car factory, however, the view would be different. The workers build cars; they do not need to know how to drive the car, but they do need to know the inner workings of car so that they can build it. This time, the abstraction becomes:

- Target of abstraction: The car.
- Target audience: Factory workers.
- What is this thing: A car is made of an engine, a fuel tank, a chasis and a bunch of other stuff.
- Relevant information: Internal structures of a car.
- Irrelevant information: How to drive a car.

As you can see, **abstraction depends on the target audience**. As the target audience changes, the definition of the target of abstraction can change, and previously relevant/irrelevant information can become irrelevant/relevant as well. Furthermore, both the definition and the relevant information depend on **expected interaction** of the target audience, i.e., what he/she/it will do with the target of abstraction: for you in a morning rush, the expected interaction is that you will drive the car to your workplace, so the relevant information are how to drive a car; for factory workers, the expected interaction is that they will build cars, so the relevant information are the internal structures of a car.

Therefore, it is always important to identify the target audience and understand what he/she/it will do with the target of abstraction, and then decide what information are relevant/irrelevant.