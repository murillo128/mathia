# MC-108 — Supercritical Hamming tails obey the same last-shell law beyond the `2 log log N` peak

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact source-forced Hamming deformation and shell coefficients of `MC-107`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
L:=\log\log N.
\]

Fix `beta>1` and let `K=K_N` satisfy

\[
\frac{K-2}{2L}\longrightarrow\beta.
\tag{1}
\]

Then the **entire alternating tail beyond `K` is asymptotically one geometric boundary layer**:

\[
\boxed{
\sum_{k>K}(-1)^k C_{k,N}
\sim
(-1)^{K+1}\frac{C_{K,N}}{1+\beta}.
}
\tag{2}
\]

Since the exact endpoint satisfies the unconditional super-logarithmic estimate already used in `MC-107`,

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\qquad\text{for every fixed }A>0,
\tag{3}
\]

the prefix through the same supercritical cutoff obeys

\[
\boxed{
\sum_{k=0}^{K}(-1)^k C_{k,N}
\sim
(-1)^K\frac{C_{K,N}}{1+\beta}.
}
\tag{4}
\]

Moreover `MC-107` gives

\[
C_{K,N}
=
N^2(\log N)^{2(\beta-1-\beta\log\beta)+o(1)},
\tag{5}
\]

so `(4)` is only a **fixed power of `log N` below `N^2`**, whereas `(3)` beats every fixed inverse power of `log N`. Thus moving a direct radial truncation any fixed proportional distance *past* the shell peak does not approach the endpoint. For every fixed `beta>1`, the omitted supercritical shells must cancel a prefix of the same asymptotic size as its last retained shell.

Combined with the subcritical law in `MC-107`, the direct-truncation obstruction now holds on both sides of the peak for every fixed proportional parameter `beta != 1`. The exactly critical turning window `beta->1` remains unresolved; this finding does **not** claim a boundary law there.

## 1. The near supercritical tail is geometrically dominated

`MC-107` proves, uniformly when the proportional parameter stays in a compact subset of `(0,infinity)`,

\[
\frac{C_{k+1,N}}{C_{k,N}}
=\left(1+o(1)\right)\frac{2L}{k-1}.
\tag{6}
\]

Choose a fixed `B>beta`. For `K<k<=2BL+O(1)`, the right side of `(6)` is eventually bounded by a constant `q<1`, because the whole interval stays a fixed positive distance to the right of the turning point. For every fixed `r>=1`, repeated use of `(6)` gives

\[
\frac{C_{K+r,N}}{C_{K,N}}\longrightarrow\beta^{-r}.
\tag{7}
\]

The uniform bound by `q^r` permits dominated convergence over the increasing finite tail up to `2BL`. Hence

\[
\begin{aligned}
\frac{(-1)^K}{C_{K,N}}
\sum_{K<k\le 2BL+O(1)}(-1)^kC_{k,N}
&\longrightarrow
\sum_{r=1}^{\infty}(-1)^r\beta^{-r}\\
&=-\frac1{1+\beta}.
\end{aligned}
\tag{8}
\]

The only remaining issue is whether degrees far beyond this compact proportional range can outweigh that geometric boundary layer.

## 2. A Selberg–Delange exponential moment kills the far shell tail

From the exact pair representation of the Hamming deformation,

\[
C_{k,N}
=
\sum_{\substack{m,n\le N\\d_\triangle(m,n)=k}}
\mu(m)^2\mu(n)^2
z\!\left(\frac{N^2}{mn}\right),
\qquad |z(x)|\le\frac12,
\tag{9}
\]

we have

\[
\sum_{k>R}|C_{k,N}|
\le
\frac12\#\left\{m,n\le N:\omega(m)+\omega(n)>R\right\},
\tag{10}
\]

because `d_triangle(m,n)<=omega(m)+omega(n)` on the square-free support.

Take `R=2BL+O(1)` and use the exponential-moment parameter `B>1`. Markov's inequality gives

\[
\sum_{k>R}|C_{k,N}|
\ll_B
B^{-2BL}
\left(\sum_{n\le N}\mu(n)^2B^{\omega(n)}\right)^2.
\tag{11}
\]

For fixed `B`, the function `mu(n)^2 B^{omega(n)}` is multiplicative and its Dirichlet series is

\[
\prod_p\left(1+\frac{B}{p^s}\right)
=\zeta(s)^B G_B(s),
\tag{12}
\]

with the usual Selberg–Delange remainder `G_B` regular and nonzero near `s=1`. The classical Landau–Selberg–Delange estimate, in the form already anchored by `MC-S14`, yields

\[
\sum_{n\le N}\mu(n)^2B^{\omega(n)}
\ll_B N(\log N)^{B-1}.
\tag{13}
\]

Therefore

\[
\sum_{k>2BL+O(1)}|C_{k,N}|
\ll_B
N^2(\log N)^{2(B-1-B\log B)}.
\tag{14}
\]

Define

\[
h(x):=x-1-x\log x.
\tag{15}
\]

For `x>1`, `h'(x)=-\log x<0`. Since `B>beta>1`, `(14)` has logarithmic exponent `2h(B)`, strictly smaller than the exponent `2h(beta)` of `C_{K,N}` in `(5)`. Thus

\[
\sum_{k>2BL+O(1)}|C_{k,N}|=o(C_{K,N}).
\tag{16}
\]

Combining `(8)` and `(16)` proves the tail law `(2)`.

## 3. The endpoint converts the tail law into a prefix obstruction

For fixed `beta>1`, `(5)` is `N^2` times one fixed power of `log N`. Choosing `A` in `(3)` larger than `-2h(beta)` gives

\[
\mathcal Q_N(1)=o(C_{K,N}).
\tag{17}
\]

Since

\[
\mathcal Q_N(1)
=
\sum_{k=0}^{K}(-1)^kC_{k,N}
+
\sum_{k>K}(-1)^kC_{k,N},
\tag{18}
\]

subtracting `(2)` from `(17)` gives `(4)`.

This proof uses no zero-free region beyond the unconditional endpoint input already present in the Hamming branch. The new tail control is purely combinatorial/large-deviation: it uses the exact shell ratio from `MC-107`, the bounded source kernel, and a classical square-free Selberg–Delange moment.

## Prior art and novelty boundary

The analytic ingredients are standard. `MC-107` already anchors the proportional Sathe–Selberg shell asymptotic and ratio law in Koukoulopoulos's treatment of Sathe–Selberg together with the standard multivariable Dirichlet-series framework. `MC-S14` anchors the Landau–Selberg–Delange transfer used in `(13)`. The passage from an exponential moment to the far-tail bound `(11)` is the classical Chernoff/Markov large-deviation device.

A targeted literature search over Sathe–Selberg large deviations, parity/truncation by the number of prime factors, and modern mod-Poisson refinements did not identify the source-specific alternating tail law `(2)` or its Hamming-endpoint consequence `(4)` as a standard named result. Modern mod-Poisson work, such as Maximilian Janisch's 2025 treatment of prime-factor counts under multiplicative weights, confirms that Selberg–Delange naturally controls central and large-deviation prime-factor statistics, but does not by itself supply this exact Möbius Hamming shell identity. **No novelty claim is made.** The durable delta is the exact continuation of the already-established radial obstruction through every fixed supercritical proportional scale.

## Boundaries and falsification tests

- The theorem requires fixed `beta>1`. The proof loses its geometric domination as `beta->1`, because the shell ratio approaches one; it does not settle the central turning window.
- The far-tail moment uses fixed `B>beta`. Allowing `beta=beta_N` or `B=B_N` to grow requires uniform Selberg–Delange control not supplied here.
- The estimate `(10)` deliberately discards the sawtooth sign and common-prime structure. That is safe only because it is used as an upper bound for a far tail already separated from the asymptotically exact near tail.
- A non-radial or genuinely global signed identity may still couple widely separated shells and evade direct-truncation logic. This result excludes only the idea that retaining all shells up to a fixed supercritical multiple of `log log N` is already close to the hard endpoint.
- The endpoint input `(3)` is unconditional and much smaller than the fixed-`beta` shell scale, but it is not an estimate for `M(N)` itself. No RH-scale Mertens bound follows.

## Consequence for the research line

The shell peak is not a one-sided frontier. `MC-107` showed that stopping at any fixed proportional scale below `2 log log N` leaves a last-shell-sized cancellation debt. The same is now true after crossing the peak by any fixed factor: for every fixed `beta>1`, the prefix and omitted tail are again asymptotically opposite boundary layers of size `C_K/(1+beta)`.

A purely radial endpoint mechanism must therefore do something more specific than "reach the peak". It must either resolve the critically tuned `beta->1` window with genuinely signed information, control a super-proportional range with uniformity beyond the fixed-parameter Sathe–Selberg regime, or introduce a nonlocal/non-radial relation that does not reduce to direct shell truncation.