# PC-291 — microscopic resonance band is spectrally invisible at square-root resolution

**Status:** `EXACT-DERIVED` + `DECISIVE-BOUNDARY` + `NEGATIVE/OBSTRUCTION` for the exact/near-resonance explanation of the `B \asymp \sqrt q` frontier left open by PC-290.

PC-271 identifies `B \asymp \sqrt q` as the first denominator-microscopic resolution at which the rank-one torus orbit necessarily develops an exact or bounded-residue integer relation. PC-290 reaches every `B=o(\sqrt q)` for the normalized boundary-log singular-spectrum law but stops at that same scale. It is therefore natural to ask whether the newly visible rational resonance itself is the missing order-one spectral mechanism.

For the actual PC-283 boundary-log finite section, the answer is negative. More strongly, **the entire microscopic residue band around the anchored collision is uniformly negligible in operator norm at the natural `1/N` matrix normalization**, even when its support contains many collisions.

Let `q` be an odd prime, let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and let `p,r` be units modulo `q`. Use the exact PC-283 profile

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0),
\]

where `|t|_q=\min(t,q-t)`, and define

\[
K_{q,B}^{p,r}(h,k)=k_q(ph+rk\bmod q),
\qquad h,k\in H_B.
\tag{1}
\]

For an integer `0\le T\le q/4`, isolate the anchored residue band

\[
K_{q,B}^{p,r,\le T}(h,k)
:=K_{q,B}^{p,r}(h,k)
\mathbf 1_{\{|ph+rk|_q\le T\}},
\tag{2}
\]

and put `K^{>T}=K-K^{\le T}`. Then

\[
\boxed{
\left\|\frac{K_{q,B}^{p,r,\le T}}{N}\right\|_{\rm op}
\le
\frac1N\left(
\log q+2\sum_{t=1}^{T}
\left|\log\!\left(2\sin\frac{\pi t}{q}\right)\right|
\right).
}
\tag{3}
\]

Consequently, for `T\ge1`,

\[
\boxed{
\left\|\frac{K_{q,B}^{p,r,\le T}}{N}\right\|_{\rm op}
\ll
\frac{\log q+T\bigl(1+\log(q/T)\bigr)}{N},
}
\tag{4}
\]

uniformly in the source pair. If `\Sigma(A)` denotes the decreasing ordered singular-value vector, the standard singular-value perturbation inequality gives

\[
\boxed{
\left\|
\Sigma\!\left(K_{q,B}^{p,r}/N\right)
-
\Sigma\!\left(K_{q,B}^{p,r,>T}/N\right)
\right\|_{\ell^\infty}
\le
\frac{
\log q+2\sum_{t=1}^{T}|k_q(t)|
}{N}.
}
\tag{5}
\]

Thus, at `B\asymp c\sqrt q` with fixed `c>0`, every fixed residue band is invisible to the complete normalized ordered singular spectrum. More generally any

\[
T=T(q)=o\!\left(\frac{\sqrt q}{\log q}\right)
\tag{6}
\]

is a sufficient uniformly invisible band in this square-root regime.

The key consequence is that the **first exact/near rational resonances guaranteed at square-root resolution cannot themselves create an order-one one-profile spectral signal**. The unresolved boundary mechanism, if one exists, must live in a wider mesoscopic part of the log-sine Green remainder or in information discarded by the one-profile singular-spectrum summary.

## 1. Each residue class is a partial permutation

Fix a residue `a mod q` and define

\[
Z_a(h,k):=\mathbf 1_{\{ph+rk\equiv a\pmod q\}},
\qquad h,k\in H_B.
\tag{7}
\]

For a fixed row `h`, the congruence in (7) determines exactly one class `k mod q` because `r` is a unit. Since `H_B` contains `N\le q` distinct residue classes, at most one such `k` lies in the window. The same argument with `p` shows that every column also contains at most one nonzero entry. Hence every `Z_a` is a partial permutation matrix and

\[
\|Z_a\|_{\rm op}\le1.
\tag{8}
\]

In particular the exact collision selector of PC-282 is `Z_0`. Because `(h,k)=(0,0)` is always present, `Z_0` is nonzero and therefore

\[
\boxed{
\left\|\frac{(\log q)Z_0}{N}\right\|_{\rm op}
=\frac{\log q}{N}.
}
\tag{9}
\]

So the exact anchored collision is already asymptotically invisible whenever `N/\log q\to\infty`, independently of any prime-source averaging.

## 2. The whole microscopic band obeys a uniform Schur bound

Equation (2) can be written exactly as

\[
K^{\le T}
=
\sum_{|a|_q\le T} k_q(a) Z_a.
\tag{10}
\]

A fixed row contains at most one entry from each residue class in the sum, and likewise for a fixed column. Therefore its maximum absolute row sum and column sum are both bounded by

\[
S_{q,T}
:=
\log q+2\sum_{t=1}^{T}
\left|\log\!\left(2\sin\frac{\pi t}{q}\right)\right|.
\tag{11}
\]

The elementary Schur bound

\[
\|A\|_{\rm op}\le
\sqrt{\|A\|_1\|A\|_\infty}
\tag{12}
\]

then gives `\|K^{\le T}\|_{op}\le S_{q,T}`, proving (3).

For `1\le t\le q/4`, the elementary sine comparison on `[0,\pi/4]` gives

\[
\left|\log\!\left(2\sin\frac{\pi t}{q}\right)\right|
\le C+\log\frac qt
\tag{13}
\]

with an absolute constant `C`. Hence

\[
\sum_{t=1}^{T}|k_q(t)|
\ll
T+T\log q-\log(T!)
\ll
T\bigl(1+\log(q/T)\bigr),
\tag{14}
\]

which proves (4). No distributional hypothesis on `p` or `r` enters the estimate.

## 3. Singular-spectrum consequence

For square matrices of the same size,

\[
\max_j|\sigma_j(A)-\sigma_j(B)|
\le\|A-B\|_{\rm op}.
\tag{15}
\]

Apply (15) to

\[
A=K/N,
\qquad
B=K^{>T}/N.
\]

Their difference is exactly `K^{\le T}/N`, so (3) gives (5). This controls every ordered singular value simultaneously. It also controls any subsequent observable that is uniformly Lipschitz for the `\ell^\infty` metric used in PC-281--PC-290.

The conclusion is deliberately representation-specific. The raw matrices `Z_a` can retain rank, support, orientation, and phase information; none of that is declared absent. The claim is only that after the established `1/N` normalization, this microscopic band cannot move the one-profile ordered singular spectrum by order one in the regimes above.

## 4. The PC-271 square-root resonance lies inside an invisible band

PC-271 defines

\[
\Delta_B(p,r;q)
=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}
\]

and proves the universal Dirichlet bound

\[
\Delta_B(p,r;q)\le\frac1{(B+1)^2}.
\tag{16}
\]

Equivalently there is a nonzero coefficient pair in the window with circular residue

\[
|hp+kr|_q
\le
\frac{q}{(B+1)^2}.
\tag{17}
\]

If `B\sim c\sqrt q`, the right side is bounded by a constant depending only on `c`. Choose any fixed integer `T` larger than that constant. Equation (5) then gives

\[
\boxed{
\left\|
\Sigma(K/N)-\Sigma(K^{>T}/N)
\right\|_{\ell^\infty}
\ll_c
\frac{\log q}{\sqrt q}
\longrightarrow0.
}
\tag{18}
\]

At the same scale PC-271's dual-lattice systole may also produce an exact nonzero resonance `hp+kr\equiv0 mod q`; it belongs to the even smaller `T=0` selector and is covered by (9).

This separates two notions that coincide geometrically but not spectrally: `B\asymp\sqrt q` is the first scale at which denominator-`q` rational relations are forced to become visible to the coefficient window, but it is **not** an amplitude threshold for the naturally normalized boundary-log singular spectrum.

## 5. Prior-art and novelty audit

No new matrix-analysis theorem is claimed. The partial-permutation observation, the Schur norm bound (12), the sine estimate (13), and singular-value perturbation (15) are classical elementary tools. The rank-one lattice/Dirichlet resonance scale is already classicalized in PC-271, while the log-sine symbol and its canonical anchor value are already classified in PC-283.

Targeted prior-art searches around log-sine finite sections, roots-of-unity cyclic kernels, rank-one lattice spectral tests, sparse resonant perturbations, and partial Fourier matrices found the expected classical neighboring ingredients but no separate theorem that changes this conclusion. The project-local content is the exact composition of those known pieces at the specific PC-290 frontier: the rational relation that first appears at `B\asymp\sqrt q` lands in a matrix band whose natural normalized operator norm tends to zero.

No `SOURCES.md` addition is needed. The result uses only already-persisted Prime-Circle dependencies plus textbook norm inequalities, and it makes no external novelty claim.

## 6. Boundary and research consequence

This finding does **not** extend the PC-290 prime-versus-count-matched-control collapse to `B\asymp\sqrt q`. It removes only one tempting explanation for why PC-290 stops there. In particular, (4) says nothing small about a band with `T` comparable to `\sqrt q/\log q` or larger, and it does not control the complement `K^{>T}`. A mesoscopic portion of the Green remainder can still interact with source placement at order one.

Nor does the result rule out architectures that retain the raw resonance support, cross-level coherence, phases, directional data, or noncommuting couplings before taking a one-profile singular spectrum. Those are explicitly outside the compression used here and remain consistent with the canonical Prime-Circle mandate.

What is ruled out is precise: **the first denominator-microscopic exact or bounded-residue collision at square-root resolution is too small, after the established `1/N` normalization, to be the missing order-one spectral carrier.** Any surviving critical-scale mechanism must therefore be mesoscopic rather than merely the onset of exact rational resonance, or must preserve information discarded by this spectral summary.