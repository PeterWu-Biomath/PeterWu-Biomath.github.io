---
layout: page
title: Open Problems
permalink: /open/
---

A list of open problems I'm interested in.

## 1. Primes of the form $n^2+1$

Are there infinitely many positive integers $n$ for which $n^2+1$ is prime?
Equivalently, are there infinitely many Gaussian primes of the form $n+i$?
This invites an analogy with Dirichlet's theorem on primes in arithmetic
progressions: might a suitable Fourier expansion reduce the question to the
analytic behavior of L-functions? The difficulty is that the condition
$\operatorname{Im}(z)=1$ is additive, whereas the characters underlying Dirichlet
and Hecke L-functions are multiplicative. An additive Fourier expansion does not
directly yield the Euler products that make those L-functions effective, so the
analogy does not immediately provide a method of proof.

## 2. Density of positive terms in a recursive sequence

Consider the following sequence: let $f_{-1}=-1$, $f_0=1$, and

$$
f_n=1-\frac{f_{n-1}}{f_{n-2}}\qquad(n\geq 1).
$$

Does the set of indices for which $f_n>0$ have natural density $3/4$? In other words, is

$$
\lim_{N\to\infty}\frac{1}{N}\#\{0\leq n<N:f_n>0\}=\frac{3}{4}?
$$

See the [Math Stack Exchange discussion](https://math.stackexchange.com/questions/5130852/).

## 3. Is $3^{3^{3^3}}+4$ prime?

Is the integer

$$
3^{3^{3^3}}+4=3^{3^{27}}+4
$$

prime? Exponentiation is interpreted from the top down.
Although the question may look like a joke, the reported computation has found
no prime divisor below $184{,}300{,}000{,}000{,}000{,}000$.
This does not establish primality, but makes the question more intriguing.

[Original discussion (in Chinese)](https://www.zhihu.com/question/554196177).

## 4. The degree-57 Moore graph

Does there exist a Moore graph of degree $57$ and diameter $2$?
Such a graph would have $57^2+1=3250$ vertices. Equivalently, does there exist
a strongly regular graph with parameters

$$
(v,k,\lambda,\mu)=(3250,57,0,1)?
$$

This is the only unresolved case in the classification of Moore graphs of
diameter $2$: the possible degrees are $2$, $3$, $7$, and $57$, and examples
are known for the first three. 

Although the question is finite, a direct search must contend with an enormous
space of possible graphs on $3250$ vertices. The common-neighbor conditions
couple choices throughout the graph, so a locally valid partial construction
may lead to a contradiction only much later. Moreover, one cannot restrict the
search to highly symmetric graphs: any such Moore graph would fail to be
vertex-transitive, ruling out many standard construction methods.

See [Brouwer's discussion of the problem and a claimed nonexistence proof](https://aeb.win.tue.nl/preprints/3250.pdf).
