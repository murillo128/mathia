# MC-279 — Positive-definite endpoint decoders have a universal half-depth source barrier

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the Boolean-row formulation of `MC-267`, `MC-275`, and `MC-278`. Write

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad x_*=1^k,
\]

so the row is blind exactly at `x=x_*`. Let

\[
D(x)=\sum_{S\subseteq[k]} a_S x_S
\tag{1}
\]

be any endpoint decoder satisfying

\[
D(x_*)=1,
\qquad
|D(x)|\le\varepsilon\quad(x\ne x_*),
\qquad
a_S\ge0\quad\text{for every }S.
\tag{2}
\]

The last condition says exactly that `D` is positive definite on the Boolean group `(\mathbb Z/2\mathbb Z)^k` in the finite-group Bochner sense. It includes the positive radial/Krawtchouk class used by the rational decoder of `MC-278`, but no radial symmetry is needed below.

Define its coefficient mass through source depth `m` by

\[
L_m(D):=\sum_{|S|\le m}a_S.
\tag{3}
\]

Since `D(x_*)=\sum_S a_S=1`, the coefficients form a probability distribution on source subsets. For every `0<\rho<1`, one has the exact universal bound

\[
\boxed{
L_m(D)
\le
\rho^{-m}
\left[
\left(\frac{1+\rho}{2}\right)^k+\varepsilon
\right].
}
\tag{4}
\]

Consequently, suppose `\varepsilon=\varepsilon_k\to0` and

\[
\log\frac1\varepsilon=o(k).
\tag{5}
\]

Then for every fixed `\delta>0`,

\[
\boxed{
L_{\lfloor(1/2-\delta)k\rfloor}(D)=o(1).
}
\tag{6}
\]

Thus the half-depth phenomenon found for the particular reciprocal-power decoder in `MC-278` is not a peculiarity of that rational function or its Gamma mixture. **Every positive-definite endpoint decoder that is uniformly sharp off the blind atom must place asymptotically all of its nonnegative Walsh/source mass at degrees at least `(1/2-o(1))k`.**

At the live blind-count scale, let

\[
C=\binom{N_y}{t}
\]

be the number of target rows. Any pointwise decoder intended to recover the integer blind count by direct summation with deterministic aggregate error below `1/2` needs

\[
\varepsilon<\frac1{2C}.
\tag{7}
\]

From `MC-275` and `MC-278`,

\[
k\sim\frac y{\log y},
\qquad
\log C
=\left(\frac1{\log2}+o(1)\right)
\log y\,\log\log y,
\tag{8}
\]

so `\log(1/\varepsilon)=O(\log C)=o(k)` at the natural atom-sensitive scale. Therefore `(6)` applies. In particular the current source depth

\[
m=t+1=\Theta(\log\log y)
\]

captures `o(1)` of the positive coefficient mass of **every** decoder satisfying `(2)`, not merely of `(1+b)^{-q}`.

For a radial decoder, `a_S=w_{|S|}` and the exact source hierarchy of `MC-267` gives

\[
\sum_{|T|=t}D(x(T))
=
\sum_{j=0}^k w_j H_{j,y}(t).
\tag{9}
\]

Hence positive-definite scalar resolvents, positive Laplace mixtures, completely monotone functions of Hamming weight, and any other endpoint decoder whose Boolean Fourier/Krawtchouk coefficients are nonnegative cannot be a hidden low-support escape from `MC-278`. A surviving scalar decoder must use **signed source coefficients** somewhere, or the argument must operate on an arithmetic/operator inverse before it becomes a positive scalar endpoint kernel.

No blind relation is excluded, no estimate for the aggregate in `(9)` is proved, and no bound for `M(X)` follows.

## 1. Noise at the blind atom measures low source depth

For `0<\rho<1`, let `T_\rho` be the standard Boolean noise operator. At the all-positive point,

\[
(T_\rho D)(x_*)
=
\sum_{S\subseteq[k]}\rho^{|S|}a_S.
\tag{10}
\]

Because every `a_S` is nonnegative,

\[
(T_\rho D)(x_*)
\ge
\rho^m\sum_{|S|\le m}a_S
=
\rho^m L_m(D).
\tag{11}
\]

The same quantity has the usual probabilistic representation. Let `Y` have independent coordinates with

\[
\Pr(Y_i=1)=\frac{1+\rho}{2},
\qquad
\Pr(Y_i=-1)=\frac{1-\rho}{2}.
\]

Then

\[
(T_\rho D)(x_*)=\mathbb E D(Y).
\tag{12}
\]

The probability of landing exactly on the blind atom is

\[
p_*(\rho)
=\Pr(Y=x_*)
=\left(\frac{1+\rho}{2}\right)^k.
\tag{13}
\]

Using `(2)`,

\[
\mathbb E D(Y)
\le
p_*(\rho)
+\varepsilon\bigl(1-p_*(\rho)\bigr)
\le
p_*(\rho)+\varepsilon.
\tag{14}
\]

Combining `(11)` and `(14)` proves `(4)`. Notice that pointwise nonnegativity of `D` is not required; the absolute off-atom bound in `(2)` is enough. Positivity is needed only in Fourier space so that the low-degree mass cannot cancel inside `(11)`.

The mechanism is therefore very simple: a positive Fourier measure concentrated at low source degree survives the noise operator strongly at `x_*`, but a decoder that is almost zero at every other cube point can survive only through the exponentially unlikely event that the noisy point remains exactly at `x_*`.

## 2. Atom sensitivity forces the mass to the middle of the source cube

Put

\[
L=\log(1/\varepsilon).
\]

Under `(5)`, fix `\delta>0`, set

\[
c=2+\delta,
\qquad
\rho=1-\frac{cL}{k},
\tag{15}
\]

and take `k` large enough that `0<\rho<1`. Then

\[
\left(\frac{1+\rho}{2}\right)^k
=
\left(1-\frac{cL}{2k}\right)^k
\le
\exp\left(-\frac c2L\right)
=
\varepsilon^{c/2}.
\tag{16}
\]

Also

\[
-\log\rho
=
\frac{cL}{k}+O\left(\frac{L^2}{k^2}\right).
\tag{17}
\]

For

\[
m\le(1/2-\delta)k,
\]

substitution into `(4)` yields

\[
L_m(D)
\le
\exp\left(
 c(1/2-\delta)L+o(L)
\right)
\left(e^{-L}+e^{-cL/2}\right).
\tag{18}
\]

Since

\[
c(1/2-\delta)
=(2+\delta)(1/2-\delta)
=1-\frac32\delta-\delta^2<1,
\tag{19}
\]

both terms in `(18)` tend to zero. This proves `(6)`.

The constant `1/2` has a structural meaning. To make a noise cloud around `x_*` miss the endpoint with probability comparable to the atom error `\varepsilon`, one must choose noise level `1-\rho` of order `2\log(1/\varepsilon)/k`. A positive Fourier character of degree `j` is damped by approximately `\exp(-(1-\rho)j)`. Balancing these two effects places the transition at `j\sim k/2`.

This argument does not identify the precise degree distribution of an arbitrary decoder. It proves only the one-sided statement needed by the research line: no fixed fraction of its positive source mass can live below `(1/2-\delta)k` while the decoder remains uniformly atom-sensitive.

## 3. `MC-278` is an instance, not the source of the barrier

For the reciprocal-power decoder

\[
F_q(x)=\frac1{(1+b(x))^q},
\]

`MC-278` obtained an explicit positive Walsh law as a Gamma mixture of binomials and computed

\[
\mathbb EJ
=\frac k2(1-2^{-q}),
\qquad
\operatorname{Var}(J)
=\left(\frac14+o(1)\right)k
\]

at atom-sensitive `q`. That explicit law gives concentration near `k/2` and is stronger than `(6)` for this particular decoder.

The present result removes everything special about that construction except **Fourier positivity and endpoint accuracy**. Rational degree, Laplace representation, radial symmetry, complete monotonicity, and the explicit Gamma law are unnecessary for the half-depth lower bound. This closes the main positive-kernel loophole left by the `MC-278` boundary statement that another rational decoder might distribute its Walsh mass differently.

It does **not** close arbitrary rational approximation. A rational decoder with signed Walsh coefficients can evade `(11)` by cancellation, and a non-scalar arithmetic inverse may not define a Boolean endpoint kernel of the form `(1)` at all. The remaining route is therefore narrower but still genuine: one needs signed cross-source cancellation, arithmetic restriction of the actual Legendre-sign image, or an intrinsic operator/resolvent estimate that does not reduce to a positive scalar decoder.

## 4. Prior art and novelty boundary

The analytic ingredients are classical. Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), DOI `10.1017/CBO9781139814782`, develops the Walsh expansion and the Boolean noise operator used in `(10)`–`(12)`. Philippe Delsarte and Vladimir I. Levenshtein, *Association schemes and coding theory*, IEEE Transactions on Information Theory 44 (1998), 2477–2504, DOI `10.1109/18.720545`, is a standard coding-theory source for the Hamming association scheme and its Krawtchouk harmonic analysis. On a finite abelian group, the equivalence between positive definiteness and nonnegative Fourier coefficients is the finite Bochner theorem.

A targeted literature search through 14 September 2026 did not locate this exact atom-sensitive inequality `(4)` or the half-depth corollary `(6)` stated for endpoint decoders on the Boolean cube. That search result is not evidence of novelty. The proof is an elementary combination of standard Fourier/noise facts, so no novelty is claimed for the abstract Boolean theorem.

The durable Mathia contribution is the frontier consequence: `MC-278`'s half-depth diagnosis extends from one convenient positive rational decoder to the entire positive-definite decoder class. Thus replacing its reciprocal power by another positive radial resolvent, completely monotone kernel, or positive Krawtchouk mixture cannot restore the logarithmic source depth needed by the current Legendre-shell route.

## Boundaries and falsification tests

- **Fourier positivity is essential.** Signed coefficients can cancel in `(10)`, so `(4)` does not apply. A signed rational or polynomial-rational decoder remains open unless another conditioning argument controls its coefficient variation.
- **Uniform endpoint accuracy is essential.** Average-case, almost-all, or shell-averaged suppression does not imply `(14)`. Such information would need a separate coupling between the noise distribution and the actual arithmetic row set.
- **The full Boolean cube remains a control, not the arithmetic image.** The theorem applies immediately to a decoder designed pointwise on all sign vectors. An arithmetic construction defined only on the tightly localized Legendre image may evade the generic cube hypothesis; `MC-252` remains the matched warning that localization must then do real work.
- **The half-depth statement concerns positive coefficient mass, not numerical contribution on nonblind rows.** Those rows may have substantial sign cancellation among high-degree characters. At the blind row all characters equal `+1`, so coefficient mass is the relevant quantity.
- **No claim about optimal signed decoders.** `(6)` is not an approximate-degree or rational-degree lower bound once coefficient signs are unrestricted.
- **No RH or Mertens consequence.** Excluding a representation class does not supply the missing arithmetic cancellation estimate.

A direct falsification would be a decoder satisfying `(2)` for which `(4)` fails, or a family satisfying `(5)` with a fixed positive fraction of nonnegative Fourier mass below `(1/2-\delta)k`. Equations `(10)`–`(19)` exclude both.

## Consequence for the research line

The representation frontier is now sharper. `MC-275` rules out generic low-degree polynomial normalization at atom-sensitive accuracy. `MC-278` showed that one low-rational-degree decoder escapes that algebraic bound only by hiding its positive Walsh mass near source depth `k/2`. The present result proves that **positive-definite scalar decoding itself is the reason for that half-depth cost**.

Accordingly, the next useful question is no longer whether a different positive rational kernel has a better source expansion. It cannot, at the scale that matters. The surviving alternatives must introduce signed source cancellation, exploit a theorem specific to the tightly localized arithmetic image, or keep the inverse as a genuinely non-scalar arithmetic/operator object rather than converting it into a positive endpoint kernel.