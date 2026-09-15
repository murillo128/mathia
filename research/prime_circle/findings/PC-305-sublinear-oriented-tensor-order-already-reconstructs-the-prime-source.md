# PC-305 — sublinear oriented tensor order already reconstructs the prime source

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` sharpening the intermediate-growing-order escape left open by PC-304.

PC-304 proves that powers of one native oriented coordinate through degree `q-1` recover the complete additive DFT and hence the source law. For the actual Prime-Circle source that upper bound is far from sharp. The source has only

\[
L_q:=|P_q|=\pi(q)-2
\]

distinct equally weighted atoms. The first `L_q` oriented power moments already recover those atoms exactly by the Newton-Girard identities. Since `L_q=O(q/\log q)`, exact source reconstruction therefore occurs at **sublinear tensor degree** even when only one frame coordinate is used. With the full window `H_B={-B,\ldots,B}`, tensor degree `d` exposes every consecutive power sum through order `dB`, so `dB\ge L_q` is already sufficient for exact reconstruction.

Thus `d(q)\ll q` is not, by itself, an intermediate information regime. A proposed growing-order Prime-Circle mechanism must stay below the source-sparsity reconstruction scale (or prevent those consecutive moments from being available), and must still specify an operation that consumes the partial packet before it becomes an exact encoding of the prime source. This is an information/classification result, not an RH mechanism.

Let `q>=5` be prime,

\[
\zeta_q=e^{2\pi i/q},\qquad
P_q=\{\ell:2<\ell<q,\ \ell\text{ prime}\},\qquad
L_q=|P_q|,
\]

and let `nu_q` be the uniform law on `P_q`. Write

\[
F_q(k):=\widehat\nu_q(k)
=\frac1{L_q}\sum_{\ell\in P_q}\zeta_q^{k\ell}.
\tag{1}
\]

As in PC-296--304, retain the native oriented frame coordinate

\[
y_s:=x_{1,s}(1)=N^{-1/2}\zeta_q^s.
\tag{2}
\]

## 1. The first `L_q` moments determine the prime support exactly

For every integer `k>=1`,

\[
\mathbb E_{s\sim\nu_q}[y_s^k]
=N^{-k/2}F_q(k).
\tag{3}
\]

Set

\[
z_\ell:=\zeta_q^\ell,
\qquad
p_k:=\sum_{\ell\in P_q}z_\ell^k=L_qF_q(k).
\tag{4}
\]

The source cardinality `L_q` is part of the finite source ensemble being averaged, so the normalized moments (3) determine `p_k` exactly. Let `e_r` be the elementary symmetric polynomial of degree `r` in the `L_q` numbers `{z_\ell: \ell\in P_q}`, with `e_0=1`. Newton's identities give recursively, for `1<=r<=L_q`,

\[
\boxed{
 r e_r
 =\sum_{k=1}^{r}(-1)^{k-1}e_{r-k}p_k.
}
\tag{5}
\]

Therefore the consecutive moments `p_1,\ldots,p_{L_q}` determine every coefficient of

\[
\boxed{
Q_q(X)
:=\prod_{\ell\in P_q}(X-z_\ell)
=X^{L_q}-e_1X^{L_q-1}+e_2X^{L_q-2}-\cdots+(-1)^{L_q}e_{L_q}.
}
\tag{6}
\]

Factoring `Q_q` recovers its distinct roots `{z_\ell}` and hence the residue set `P_q` itself. Consequently

\[
\boxed{
\{\mathbb E[y^k]:1\le k\le L_q\}
\Longrightarrow
P_q\ \text{exactly}.
}
\tag{7}
\]

This is strictly stronger than the generic `q-1` Fourier-inversion saturation in PC-304. It uses the actual equal-weight sparse structure of the canonical Prime-Circle source rather than treating `nu_q` as an arbitrary law on all `q` residues.

No asymptotic or prime-number theorem enters the reconstruction itself. The implication (7) is a finite algebraic identity at each prime modulus.

## 2. The required tensor degree is already sublinear

For the canonical source,

\[
L_q=\pi(q)-2.
\tag{8}
\]

The classical Chebyshev upper bound already gives

\[
\pi(q)=O\!\left(\frac q{\log q}\right),
\]

so

\[
\boxed{L_q=o(q).}
\tag{9}
\]

Combining (3)--(7), powers of the **single** coordinate `y_s` through degree

\[
d=L_q=\pi(q)-2
\tag{10}
\]

already reconstruct the complete prime support. Hence there is an explicitly source-forced sublinear sequence `d(q)<<q` at which the growing tensor hierarchy has already saturated informationally.

This corrects the scale interpretation left open by PC-304. Its statement that degree `q-1` suffices is valid, but `d(q)<<q` cannot be used as a proxy for "far from source reconstruction" on the canonical prime source.

## 3. The spatial frame window lowers the saturation degree further

The full PC-296--304 frame has

\[
H_B=\{-B,\ldots,B\}
\]

and, for the `m=1` mode,

\[
x_{1,s}(h)=N^{-1/2}\zeta_q^{sh}.
\tag{11}
\]

Take a degree-`d` monomial using the same source residue `s`:

\[
T_{h_1,\ldots,h_d}(s)
:=\prod_{j=1}^d x_{1,s}(h_j)
=N^{-d/2}\zeta_q^{s(h_1+\cdots+h_d)}.
\tag{12}
\]

Averaging gives

\[
\boxed{
\mathbb E_{\nu_q}T_{h_1,\ldots,h_d}
=N^{-d/2}F_q(h_1+\cdots+h_d).
}
\tag{13}
\]

Because `0,1,\ldots,B` are all available window coordinates, every integer

\[
1\le k\le dB
\]

can be written as a sum of `d` integers in `[0,B]`; zeros simply pad a shorter representation. Thus degree `d` already exposes the entire consecutive packet

\[
F_q(1),\ldots,F_q(dB).
\tag{14}
\]

Applying the Newton reconstruction above yields the sufficient saturation condition

\[
\boxed{
 dB\ge L_q
 \quad\Longrightarrow\quad
 \text{the degree-}d\text{ oriented-frame tensor packet determines }P_q\text{ exactly}.
}
\tag{15}
\]

Equivalently,

\[
\boxed{
 d_{\rm sat}(q,B)
 \le
 \left\lceil\frac{\pi(q)-2}{B}\right\rceil.
}
\tag{16}
\]

For a fixed nontrivial window this is already `O(q/log q)`. If `B=B(q)` grows, the required tensor order falls proportionally. For example, a square-root window `B\asymp q^{1/2}` gives the sufficient scale

\[
d_{\rm sat}=O\!\left(\frac{q^{1/2}}{\log q}\right).
\tag{17}
\]

The same observation can be phrased in the frequency-alphabet language of PC-303: products add the represented additive characters before averaging. Equation (15) is the source-specific consequence that matters here.

## 4. What this does and does not close

The result closes a substantial part of the vague "intermediate `d(q)<<q`" escape left by PC-304. There are now three qualitatively different statements:

- fixed tensor degree classicalizes to a finite Fourier/polyspectral packet (PC-303);
- growing degree need not reach order `q`: at degree `L_q=O(q/log q)`, and at degree `O(L_q/B)` with a width-`B` frame, the canonical source is already exactly reconstructible (this finding);
- once source reconstruction has occurred, any subsequent determinant, spectrum, nonlinear statistic, or cross-level post-processing must be justified as a new geometry-forced operation rather than as information gain from the tensor hierarchy itself.

This does **not** prove that every regime with `dB<L_q` is non-reconstructive. The Prime-Circle source is highly special, and nonconsecutive Fourier data or arithmetic side information could in principle identify it earlier. Equation (15) is a sharp enough **sufficient** reconstruction mechanism to invalidate `d=o(q)` as a meaningful standalone notion of an intermediate phase; it is not claimed as a necessary threshold.

Nor does exact recovery of `P_q` provide an RH bridge. It reconstructs which lower residues are prime. It creates no spectral parameter, gamma factor, functional equation, explicit-formula kernel, or critical-line constraint.

## 5. Prior-art and novelty audit

The algebraic mechanism is classical. Newton-Girard identities recover the coefficients of a degree-`L` polynomial from the first `L` power sums of its roots, and Prony-type methods generalize the same principle to finitely supported measures and exponential sums. A direct prior-art search therefore places the reconstruction step squarely inside classical power-sum/sparse-moment recovery, not as new mathematics.

The project-local contribution is the scale boundary inside the Prime-Circle oriented-frame hierarchy: **because the actual source is an equally weighted set of only `L_q=pi(q)-2` roots, the supposedly intermediate growing-order regime reaches exact source reconstruction already at sublinear degree, with the spatial window reducing the sufficient degree by another factor `B`.** PC-304's generic full-DFT argument does not state this source-sparsity saturation.

The proof is self-contained; the literature audit is neighboring prior art rather than a load-bearing dependency, so no new `SOURCES.md` anchor is required.

## 6. Falsification and finite controls

The central claim has a direct exact test. For any prime `q`, compute `F_q(k)` for `1<=k<=L_q`, form `p_k=L_qF_q(k)`, apply recursion (5), and factor (6). The recovered roots must be exactly `{zeta_q^ell: ell in P_q}`. Direct numerical checks at `q=13`, `29`, and `101` recover respectively

\[
\{3,5,7,11\},
\]

\[
\{3,5,7,11,13,17,19,23\},
\]

and the full 24-element prime support below `101` (excluding `2`) to floating-point root accuracy.

Equation (13) is independently falsifiable by choosing arbitrary `h_1,\ldots,h_d` and comparing the averaged frame monomial with `F_q(\sum h_j)`. If any consecutive frequency `1<=k<=dB` cannot be realized when `H_B={-B,\ldots,B}`, then (15) fails; the explicit decomposition into summands in `[0,B]` rules this out.

## 7. Consequence for the live frontier

A genuinely intermediate growing-tensor proposal must now specify more than `d(q)<<q`. At minimum it must track the joint resolution parameter `d(q)B(q)` (or the actual additive frequency alphabet of the chosen frame) against the source sparsity `L_q`. If the construction exposes `L_q` consecutive power sums, it has already become an exact encoding of the prime source and any later RH claim must come from a separately identified operation.

The remaining potentially nontrivial target is therefore a regime in which the available frequency packet is still incomplete **and** a geometry-forced operation consumes that partial packet before classical Newton/Prony reconstruction or per-modulus source recovery becomes available. Genuinely cross-level/mixed-conductor coupling remains outside this result, as does any nonlinear evolution that is not equivalent to forming and then post-processing these source moments.