# ANF-190 — Height mean values confine bow endpoint memory to sparse twists

**Status:** LITERATURE+DERIVED + EXACT-HEIGHT-MEAN-SQUARE + MAXIMAL-PREFIX-BOUND + HEIGHT-SPARSE-EXCEPTION + DISTINGUISHED-HEIGHT-LIMITATION.

The bow endpoint completion of ANF-157 is large only on a quantitatively sparse set of twist heights, even when no cancellation of the actual prime-minus-Ramanujan residual is assumed. The input is the source-specific local quadratic-mass bound from ANF-162, combined with the classical Montgomery–Vaughan separated-frequency mean-value inequality. An elementary dyadic maximal argument controls every endpoint prefix simultaneously and, by ANF-185, every triangular high-pass aperture simultaneously. This result is **about averaging the twist height**: it does not place the prescribed bow height outside the exceptional set, nor does it bound the moving-window bow variance at that height.

## 1. Statement for the actual endpoint source

Fix (0<\varepsilon<1/16) and let (K=K(X)\in\mathbb N) satisfy
[
K=X^{1-2\varepsilon+o(1)},\qquad 2\le K\le X/4.
\tag{1}
]
Use the residual of ANF-149 and ANF-162:
[
R=\exp((\log X)^{1/10}),\quad
P(R)=\prod_{p<R}p,\quad
Q_R(n)=\frac{P(R)}{\varphi(P(R))}{\bf1}_{(n,P(R))=1},\quad
r_X(n)=\vartheta(n)-Q_R(n),
\tag{2}
]
where (\vartheta(n)=\log n) if (n) is prime and (0) otherwise. For the integer finite-horizon model of ANF-157, put
[
n_j^-=X+j,\qquad n_j^+=2X+K-j,\qquad
P_m^\sigma(U)=\sum_{j=1}^m r_X(n_j^\sigma)(n_j^\sigma)^{-iU},
\quad 1\le m<K,\quad \sigma\in\{-,+\},
\tag{3}
]
and
[
E_\partial(U)
=\sum_{m=1}^{K-1}\left(|P_m^-(U)|^2+|P_m^+(U)|^2\right),\qquad
\mathcal M(U)=\max_{\sigma\in\{-,+\},,1\le m<K}|P_m^\sigma(U)|.
\tag{4}
]
Here (E_\partial) is exactly the two-sided missing-row completion in ANF-157, and (\mathcal M) is its maximal endpoint prefix amplitude.

For **every** real interval (I=[U_0,U_0+L]) of length (L>0), with constants independent of (U_0,L),
[
\boxed{\displaystyle
\int_I E_\partial(U)\,dU
\ll (L+X)K^2\log X,
}
\tag{5}
]
and
[
\boxed{\displaystyle
\int_I\mathcal M(U)^2\,dU
\ll (L+X)K\log X\,[\log(2K)]^2.
}
\tag{6}
]
In particular, for any fixed (\tau,\eta>0) and (a_X=\sqrt{\delta X\log X}) with fixed (\delta>0),
[
\boxed{\displaystyle
\operatorname{meas}\{U\in I:E_\partial(U)\ge\tau XK\log X\}
\ll_\tau (L+X)\frac KX,
}
\tag{7}
]
[
\boxed{\displaystyle
\operatorname{meas}\{U\in I:\mathcal M(U)\ge\eta a_X\}
\ll_{\delta,\eta}(L+X)\frac KX[\log(2K)]^2.
}
\tag{8}
]
Thus for (L\ge X), the exceptional *proportions* are respectively
(O_\tau(K/X)) and (O_{\delta,\eta}(K\log^2(2K)/X)), both
(X^{-2\varepsilon+o(1)}\to0). Choosing slowly vanishing thresholds in (7)–(8) shows, for almost all heights in any such interval, simultaneously
[
E_\partial(U)=o(XK\log X),\qquad \mathcal M(U)=o(a_X).
\tag{9}
]
Here “almost all” means relative measure tending to one, not a claim about a distinguished single height.

## 2. The actual prime–rough source has the required edge quadratic mass

On either endpoint block in (3), all integers lie in ([X,3X]) and the block length is at most (K). Brun–Titchmarsh on a fixed polynomial-length interval gives
[
\#\{p\in J\}\ll \frac{K}{\log K}
\qquad (|J|\le K,\ J\subset[X,3X])
\tag{10}
]
when (J) is the full endpoint block of length (K-1); smaller subblocks are not needed for the following argument. Since (|\vartheta(n)|\le\log(3X)) and (Q_R(n)\le c_R:=P(R)/\varphi(P(R))\ll\log R\ll(\log X)^{1/10}),
[
\begin{aligned}
S_2&:=\sum_{j=1}^{K-1}\bigl(
 |r_X(n_j^-)|^2+|r_X(n_j^+)|^2\bigr)\\
&\ll \frac{K(\log X)^2}{\log K}
      +K(\log X)^{1/5}
\ll K\log X.
\end{aligned}
\tag{11}
]
The final step uses (\log K\asymp\log X). No signed prime correlation or averaging hypothesis is used. Equation (11) is consistent with, and is a direct full-block specialization of, the source local-(L^2) estimate of ANF-162.

## 3. Separated logarithmic frequencies give the endpoint mean-square estimate

For arbitrary distinct integers (n_j\in[X,3X]), set (\lambda_j=\log n_j). Their minimum frequency separation is
[
\min_{j\ne k}|\lambda_j-\lambda_k|\ge\frac1{3X}
\tag{12}
]
for sufficiently large (X). Montgomery–Vaughan's Hilbert inequality, applied to the two boundary terms of the integrated off-diagonal expansion, gives the finite exponential-polynomial mean-value bound
[
\boxed{\displaystyle
\int_{U_0}^{U_0+L}
\left|\sum_{j\in J}d_j e^{-iU\lambda_j}\right|^2dU
\le (L+CX)\sum_{j\in J}|d_j|^2
}
\tag{13}
]
for any coefficient subset (J), with one absolute (C). Indeed, the diagonal integrates to (L\sum|d_j|^2); integrating a cross term produces the difference of two forms with denominator (i(\lambda_j-\lambda_k)), and the separated-frequency Hilbert bound controls each form by (O(X)\sum|d_j|^2). This bound remains valid in reverse physical order and for arbitrarily short (I).

Apply (13) to every prefix in (3) and sum over (m). Each coefficient occurs in at most (K-1) such prefixes, so
[
\begin{aligned}
\int_I E_\partial(U)dU
&\ll (L+X)\sum_{\sigma}\sum_{m<K}\sum_{j\le m}|r_X(n_j^\sigma)|^2\\
&\le (L+X)K S_2
\ll (L+X)K^2\log X,
\end{aligned}
\tag{14}
]
which is (5).

## 4. A dyadic maximal inequality controls every prefix and every aperture

Write (N=K-1) and pad the coefficient sequence in (3) by zeros to the next power of two. Every prefix ([1,m]) is a disjoint union of at most (d=\lceil\log_2(2K)\rceil) aligned dyadic blocks. Cauchy–Schwarz, followed by summation over **all** blocks in the dyadic tree, shows pointwise
[
\max_{m\le N}|P_m^\sigma(U)|^2
\le d\sum_{B\text{ dyadic}}
\left|\sum_{j\in B}r_X(n_j^\sigma)e^{-iU\log n_j^\sigma}\right|^2.
\tag{15}
]
At every fixed dyadic level the blocks are disjoint. Integrating each block with (13) and summing over the (d) levels gives
[
\int_I\max_{m\le N}|P_m^\sigma(U)|^2dU
\ll d^2(L+X)\sum_{j\le N}|r_X(n_j^\sigma)|^2.
\tag{16}
]
Summing over the two endpoints and invoking (11) proves (6). This is the finite elementary dyadic step underlying the classical Rademacher–Menshov maximal inequality; no orthogonality of the prime coefficients is assumed.

For the exact distinguished-height, fixed-base high-pass of ANF-185, let
[
\mathcal D_T(r_X;U)
=\sum_{j=0}^{K}r_X(X+j)e^{-iU\log(1+j/X)}
 W\left(T\log(1+j/X)\right),\quad
W(y)=1-\operatorname{sinc}^2(y/2).
\tag{17}
]
ANF-185 proves (W(0)=0) and uniformly bounded variation of the weight sequence for **every** (T>0). Abel summation therefore gives, including the one extra (j=K) coefficient,
[
\boxed{
\sup_{T>0}|\mathcal D_T(r_X;U)|
\ll \mathcal M(U)+O(\log X).
}
\tag{18}
]
The change from (n^{-iU}) to ((n/X)^{-iU}) is a common unit phase; it does not change prefix magnitudes. Since (\log X=o(a_X)), (8) controls **simultaneously all apertures** of this detector at the (a_X) scale. There is no uncountable-union error: one maximal prefix bound already dominates the complete (T)-family.

Finally Markov's inequality applied to (5) and (6) gives (7)–(8). For a sequence of intervals satisfying
[
\frac{L}{K[\log(2K)]^2}\longrightarrow\infty,
\tag{19}
]
we have ((L+X)K\log^2(2K)/(LX)\to0) because (K\log^2K=o(X)). Hence **every** such interval contains at least one height with (\mathcal M(U)=o(a_X)), and all the high-passes in (17) are (o(a_X)) there. One may, for example, take (L=K\log^3K=o(X)). This produces nearby good heights, not a bound at the interval center.

## 5. Adversarial boundary, prior art, and consequence

The external tools are classical. The frequency-separated Hilbert inequality is from H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73–82, DOI 10.1112/jlms/s2-8.1.73 (already anchored in SOURCES.md). The dyadic maximal mechanism has its classical origin in H. Rademacher, *Einige Sätze über Reihen von allgemeinen Orthogonalfunktionen*, Math. Ann. 87 (1922), 112–138, DOI 10.1007/BF01458040; the finite estimate needed here is proved directly in (15)–(16). The source-specific (L^2) input is the Brun–Titchmarsh calibration of ANF-162. This is **not a new mean-value theorem for Dirichlet polynomials**. The Mathia-specific conclusion is the exact (K/X) exceptional-height budget for the two missing-row bow endpoint squares, together with a simultaneous control of the entire ANF-185 high-pass aperture family.

The quantifiers are decisive. A negligible exceptional *proportion* is compatible with a prescribed height (U(X)\asymp X^2) belonging to the exceptional set for every (X). The carrier-aware signed matched controls of ANF-186 and the opposed packets of ANF-189 illustrate why source-independent twist-averaging cannot be substituted for a theorem about the actual distinguished prime/rough placement. The original bow moving-window variance is also a different quantity: ANF-102 shows that its average over long height windows retains a full prime diagonal. A small *endpoint correction* at typical heights does not imply a small *moving-window variance* there.

Thus (5)–(19) close a precise generic-height question but leave the RH-facing arithmetic gate unchanged: show that the distinguished height itself avoids the rare endpoint-coherent configurations, or establish a coupled signed Fejér-slope/source-correlation theorem as in ANF-172. No finite-height exclusion of off-critical zeta zeros follows.
