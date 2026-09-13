# MC-268 — A Krawtchouk–Christoffel endpoint detector removes the Gaussian moment penalty

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `CANDIDATE-NEW-STRUCTURE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell notation of `MC-264`–`MC-267`. For

\[
T\in\binom{\mathcal R_y}{t},
\qquad
b_y(T)=\#\{p\in\mathcal P_y:\sigma_p(T)=-1\},
\]

recall that a blind shell relation is exactly the endpoint event

\[
b_y(T)=0.
\]

`MC-264` tested that event with the monomial moment `B_y(T)^{2m}`, while `MC-267` showed that all source-support aggregates through degree `2m` are simply another basis for the same truncated shell-amplitude distribution. There is a strictly better positive detector at the **same source-depth budget**: the Christoffel extremal polynomial for the binomial/Krawtchouk measure.

Let

\[
\nu_k(b)=2^{-k}\binom kb,
\qquad 0\le b\le k,
\]

and use the binary Krawtchouk normalization

\[
K_s(b;k)=\sum_{j=0}^s(-1)^j\binom bj\binom{k-b}{s-j}.
\]

For `0\le m\le k`, define

\[
Z_m(k)=\sum_{s=0}^m\binom ks,
\tag{1}
\]

\[
R_m(b;k)=\sum_{s=0}^m K_s(b;k),
\qquad
P_m(b;k)=\frac{R_m(b;k)}{Z_m(k)}.
\tag{2}
\]

Then exactly

\[
P_m(0;k)=1
\tag{3}
\]

and

\[
\boxed{
\sum_{b=0}^k\nu_k(b)P_m(b;k)^2
=\frac1{Z_m(k)}.
}
\tag{4}
\]

Moreover `(4)` is optimal among all degree-`m` polynomial squares anchored at the blind endpoint: if `P` has degree at most `m` and `P(0)=1`, then

\[
\boxed{
\sum_{b=0}^k\nu_k(b)P(b)^2
\ge\frac1{Z_m(k)}.
}
\tag{5}
\]

Thus `P_m^2` is the minimum-binomial-mass positive square certificate for a point mass at `b=0`.

Apply this detector to the actual shell histogram. Set

\[
\mathcal E_{m,y}(t)
=
\sum_{|T|=t}P_m\!\left(b_y(T);k_y\right)^2.
\tag{6}
\]

Since every blind `T` contributes exactly one and every term is nonnegative,

\[
\boxed{
A_y(t)\le \mathcal E_{m,y}(t).
}
\tag{7}
\]

The square in `(6)` has degree at most `2m`, so by `MC-267` there are explicit classical Krawtchouk linearization coefficients `\gamma_{m,s}(k_y)` such that

\[
P_m(b;k_y)^2
=
\sum_{s=0}^{2m}\gamma_{m,s}(k_y)K_s(b;k_y),
\]

hence exactly

\[
\boxed{
\mathcal E_{m,y}(t)
=
\sum_{s=0}^{2m}\gamma_{m,s}(k_y)H_{s,y}(t).
}
\tag{8}
\]

No new information has been created by the change of polynomial. The gain is that the available low-support information is combined in the **endpoint-optimal positive way** instead of being committed to the single monomial `B^{2m}`.

If a future arithmetic theorem proves the binomial-scale estimate

\[
\boxed{
\mathcal E_{m,y}(t)
\le
L_y\frac{\binom{N_y}{t}}{Z_m(k_y)},
}
\tag{9}
\]

then `(7)` rules out every weight-`t` blind relation whenever

\[
L_y\frac{\binom{N_y}{t}}{Z_m(k_y)}<1.
\tag{10}
\]

At the live scale

\[
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\tag{11}
\]

this changes the threshold ledger from `MC-264` in two ways.

First, `m=t` is no longer exponentially above the single-atom scale. In fact

\[
\boxed{
\frac{\binom{N_y}{t}}{Z_t(k_y)}
=
1-\frac{2\log\log y}{\log y}
+o\!\left(\frac{\log\log y}{\log y}\right).
}
\tag{12}
\]

Thus degree `2t` is the **first endpoint-adapted square degree that reaches the natural one-atom threshold**. An extraordinarily sharp arithmetic comparison with relative loss

\[
L_y=1+o\!\left(\frac{\log\log y}{\log y}\right)
\tag{13}
\]

would already make `(10)` hold at `m=t`. By contrast, every `m\le t-1` has

\[
\frac{\binom{N_y}{t}}{Z_m(k_y)}\to\infty,
\tag{14}
\]

so the binomial baseline itself is too large there.

Second, retaining the safer one-extra-degree choice `m=t+1` gives

\[
\boxed{
\frac{\binom{N_y}{t}}{Z_{t+1}(k_y)}
=
(1+o(1))\frac{t+1}{k_y}
=
\frac{(1+o(1))(t+1)\log y}{y}.
}
\tag{15}
\]

Hence `(9)` excludes blind support whenever, for example,

\[
L_y=o\!\left(\frac{k_y}{t+1}\right).
\tag{16}
\]

This is a larger admissible loss than the monomial-moment condition in `MC-264`, which at `m=t+1` pays the quadratic/Rademacher factor and has normalized natural scale

\[
(1+o(1))\frac{2^{t+1}\sqrt{t/\pi}}{k_y}.
\]

The Christoffel detector improves that natural baseline by the factor

\[
\boxed{
\frac{2^{t+1}}{\sqrt{\pi t}}(1+o(1)),
}
\tag{17}
\]

which is of order `log y/sqrt(log log y)` at `(11)`.

The durable conclusion is therefore not a new blind-support exclusion. It is a correction of the **detector** at the current frontier: the `2t` monomial moment in `MC-264` is too expensive because it is not endpoint-optimal, not because degree `2t` intrinsically lacks enough resolution. The exact low-support frontier should now ask for arithmetic control of the Christoffel-weighted combination `(8)` (or a still stronger source-specific positive certificate), rather than treating `B^{2m}` as the canonical high-moment test.

No blind relation is excluded here, no estimate for `M(X)` follows, and `(9)` is not proved.

## 1. Krawtchouk orthogonality gives the endpoint kernel exactly

For the probability measure `\nu_k`, binary Krawtchouk orthogonality is

\[
\sum_{b=0}^k
\nu_k(b)K_r(b;k)K_s(b;k)
=
\binom ks\mathbf 1_{r=s}.
\tag{18}
\]

Also

\[
K_s(0;k)=\binom ks.
\tag{19}
\]

Therefore the degree-`m` reproducing kernel evaluated against the endpoint `0` is

\[
\mathcal K_m(b,0)
=
\sum_{s=0}^m
\frac{K_s(b;k)K_s(0;k)}{\binom ks}
=
\sum_{s=0}^mK_s(b;k)
=R_m(b;k).
\tag{20}
\]

Its endpoint diagonal is

\[
\mathcal K_m(0,0)=Z_m(k).
\tag{21}
\]

Dividing `(20)` by `(21)` gives `(2)` and `(3)`. Orthogonality then gives

\[
\|P_m\|_{L^2(\nu_k)}^2
=
\frac1{Z_m(k)^2}
\sum_{s=0}^m\binom ks
=
\frac1{Z_m(k)},
\]

which proves `(4)`.

For any polynomial `P` of degree at most `m`, the reproducing property gives

\[
P(0)=\langle P,R_m(\cdot;k)\rangle_{L^2(\nu_k)}.
\]

If `P(0)=1`, Cauchy–Schwarz and `\|R_m\|_2^2=Z_m(k)` imply

\[
1\le \|P\|_2\sqrt{Z_m(k)},
\]

proving `(5)`. Equality holds exactly for the normalized kernel `P_m`.

This is the ordinary Christoffel-function extremal problem specialized to the binomial/Krawtchouk measure. No arithmetic input enters `(1)`–`(5)`.

## 2. The detector uses exactly the same truncated arithmetic data

Equation `(8)` is important because it prevents a false interpretation of the improvement. `P_m^2` has degree at most `2m`, so its shell sum is determined completely by

\[
H_{0,y}(t),\ldots,H_{2m,y}(t),
\]

which `MC-267` identified as the Krawtchouk transform of the shell-amplitude histogram. The Christoffel detector therefore does not evade the information-neutrality result of `MC-267`; it exploits that information optimally for the specific endpoint question.

The monomial detector of `MC-264` uses

\[
\left(\frac{B_y(T)}{k_y}\right)^{2m}
=
\left(1-\frac{2b_y(T)}{k_y}\right)^{2m},
\]

which is also a nonnegative degree-`2m` polynomial equal to one at `b=0`. Under the binomial comparator its mass is the normalized `2m`-th Rademacher moment, asymptotic to

\[
\frac{(2m-1)!!}{k_y^m}
\]

when `m^2=o(k_y)`. The Christoffel extremality `(5)` shows directly why this pays an avoidable Gaussian pairing factor: among degree-`m` anchored polynomials, the normalized endpoint kernel has squared mass `1/Z_m(k_y)`, asymptotic to

\[
\frac{m!}{k_y^m}.
\tag{22}
\]

Their ratio is

\[
\frac{(2m-1)!!}{m!}
=
\frac{\binom{2m}{m}}{2^m}
\sim
\frac{2^m}{\sqrt{\pi m}},
\tag{23}
\]

exactly the factor that made the pure `2t` moment look too coarse in `MC-264`.

This also explains why the useful object after `MC-267` is not an arbitrary new Krawtchouk recurrence. The coefficients in `(8)` are selected by a precise extremal problem: minimize the null/binomial `L^2` mass subject to unit response at the blind endpoint.

## 3. Threshold asymptotics

Because `t=O(\log\log y)` while `k_y\asymp y/\log y`, we have `t^2=o(k_y)`. Uniformly for `m=t+O(1)`,

\[
Z_m(k_y)
=
\binom{k_y}{m}\left(1+O\!\left(\frac m{k_y}\right)\right)
=
(1+o(1))\frac{k_y^m}{m!}.
\tag{24}
\]

The two-term prime number theorem expansion gives, with `L=\log y`,

\[
k_y
=
\frac yL\left(1+\frac1L+O(L^{-2})\right),
\tag{25}
\]

\[
N_y
=
\frac yL\left(1+\frac{1-2\log2}{L}+O(L^{-2})\right),
\tag{26}
\]

and hence

\[
\frac{N_y}{k_y}
=
1-\frac{2\log2}{L}+O(L^{-2}).
\tag{27}
\]

For `m=t`, equations `(24)` and `(27)` give

\[
\frac{\binom{N_y}{t}}{Z_t(k_y)}
=
\left(\frac{N_y}{k_y}\right)^t
\left(1+o\!\left(\frac{t}{L}\right)\right)
=
1-\frac{2(\log2)t}{L}+o\!\left(\frac tL\right).
\tag{28}
\]

Substituting `(11)` proves `(12)`.

For `m=t-1`, the same calculation gives

\[
\frac{\binom{N_y}{t}}{Z_{t-1}(k_y)}
=
(1+o(1))\frac{k_y}{t}
\left(\frac{N_y}{k_y}\right)^t
\longrightarrow\infty.
\tag{29}
\]

Since `Z_m(k_y)` increases with `m`, `(29)` implies `(14)` for every `m\le t-1`.

For `m=t+1`, use

\[
\binom{k_y}{t+1}
=
\binom{k_y}{t}\frac{k_y-t}{t+1}
\]

in `(24)` to obtain

\[
\frac{\binom{N_y}{t}}{Z_{t+1}(k_y)}
=
(1+o(1))
\frac{t+1}{k_y}
\left(\frac{N_y}{k_y}\right)^t,
\]

and `(15)` follows because the final power tends to one.

## 4. Prior art and novelty boundary

The mathematical mechanism is classical. Krawtchouk polynomials are the orthogonal polynomials of the binomial measure, and their relation to Boolean-cube weight distributions and Walsh characters is standard; Alex Samorodnitsky, *Weight distribution of random linear codes and Krawtchouk polynomials*, Random Structures & Algorithms 64 (2024), DOI `10.1002/rsa.21214`, is a modern reference already adjacent to `MC-264`–`MC-267`.

The reproducing-kernel construction, the reciprocal diagonal kernel as the Christoffel function, and the minimum-`L^2` point-evaluation characterization used in `(4)`–`(5)` are standard orthogonal-polynomial theory. Jean-Bernard Lasserre, Edouard Pauwels and Mihai Putinar, *The Christoffel–Darboux Kernel for Data Analysis*, Cambridge University Press (2022), especially Chapters 2, 3 and 10, DOI `10.1017/9781108937078`, treats the kernel, bounded point evaluation, moment problems and the Christoffel extremal viewpoint.

The coding-theory use of Krawtchouk expansions and positive polynomial certificates belongs to Delsarte's linear-programming/association-scheme framework; see Philippe Delsarte, *An algebraic approach to the association schemes of coding theory*, Philips Research Reports Supplements 10 (1973). Modern Delsarte work continues to formulate code constraints and dual certificates directly in Krawtchouk coordinates.

A targeted literature search through 13 September 2026 found the classical Christoffel extremal theory, Krawtchouk Christoffel–Darboux kernels, Delsarte positive-polynomial methods, and modern Krawtchouk weight-distribution literature. No novelty is claimed for any of those ingredients. The durable Mathia delta is the **frontier calibration for the exact Legendre shell problem**: applying the binomial endpoint Christoffel detector to `MC-267` shows that the Gaussian/Rademacher factor in `MC-264` is detector-dependent, places degree `2t` exactly at the one-blind-atom threshold, and enlarges the admissible analytic-loss budget at degree `2(t+1)` by `(17)`.

## 5. Boundaries and decisive next test

- **No arithmetic estimate is proved.** Equation `(9)` is the missing theorem; classical Christoffel/Krawtchouk algebra alone says nothing about whether the actual Legendre shell histogram has binomial-scale detector energy.
- **No contradiction with `MC-267`.** The detector is an optimized combination of the same truncated `H_s` data. It does not create new information.
- **The `m=t` gain is fragile.** Its natural baseline lies below one only by order `log log y/log y`; any ordinary polylogarithmic multiplicative loss destroys that advantage.
- **The `m=t+1` gain is robust.** It leaves the much larger budget `(16)` and strictly improves the monomial baseline without increasing the maximum source-support degree.
- **Odd source layers may enter.** Unlike `B^{2m}`, the endpoint kernel is not symmetric under `b -> k-b`; its square can use both odd and even Krawtchouk layers. This is appropriate because the blind endpoint `b=0` is not the anti-endpoint `b=k`, but any analytic proof of `(9)` must account for those layers rather than silently discard them.
- **Christoffel optimality is comparator-relative.** Equation `(5)` is optimal for squared degree-`m` polynomials under the binomial measure. The actual arithmetic histogram is not assumed binomial, and a source-specific positive certificate outside this class could be stronger.
- **No RH-scale conclusion follows.** Even a blind-support exclusion at this shell stage would still need the already-audited transfer from generation/signed rough cancellation to the global Möbius zero mode.

The decisive next test is now sharper than the one after `MC-267`: derive or refute `(9)` for `m=t` or `m=t+1` using genuine arithmetic information about the lower-prime Legendre sign image. A successful proof should act directly on the Christoffel-weighted mixture `(8)` or on an equivalent non-radial representation, and must beat the binomial baseline by arithmetic cancellation rather than by another universal Krawtchouk identity.