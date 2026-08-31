# WI-065 — redundant common refinements still incur a super-polylogarithmic Mikawa cost

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`, with the arithmetic square-function bridge inherited from WI-061 and therefore retaining WI-061's `NEEDS-AUDIT` boundary. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, change Mathia's current unconditional simple-critical proportion, or rule out a genuinely residue-averaged/vector-valued prime-pair theorem. It closes a broader version of the first escape left open by WI-064: even if one is allowed to represent every exact Fourier conductor redundantly inside many common refinement moduli, and even if the non-reduced-residue nuisance is granted away for free, combining those refinements through only Mikawa's modulus-weighted residue-max square-function budget and generic Hilbert/Cauchy assembly still has a super-polylogarithmic coefficient.

The key point is an exact weighted-frame lower bound. If a mode of reduced conductor `d` is split among all refinement moduli `Q` divisible by `d`, the best possible quadratic cost is controlled by

\[
\left(\sum_{\substack{Q\le Q_*\\d\mid Q}}\frac1Q\right)^{-1}.
\]

There are at most harmonically many such lifts, so

\[
\boxed{
\left(\sum_{\substack{Q\le Q_*\\d\mid Q}}\frac1Q\right)^{-1}
\ge
\frac{d}{1+\log Q_*}.
}
\]

Thus arbitrary redundancy can save at most one logarithm over the diagonal conductor weight `d B_d`. WI-059 proves that every asymptotically lossless `W`-local spectral family has a `d B_d` cost larger than every fixed power of `log X`; dividing by `1+log Q_* = O(log X)` leaves it super-polylogarithmic. Hence Mikawa's arbitrary **fixed** logarithmic saving still cannot close the splice through this architecture.

## 1. Exact source interface from WI-064

Use the all-residue pair errors and normalized Fourier coefficients of WI-064. For odd squarefree `d|Q`, the exact divisor-martingale identity gives

\[
\widetilde T_{Q,cQ/d}(H)=\widetilde T_{d,c}(H)
\tag{1}
\]

for every reduced frequency `c mod d`. Distinct reduced rational frequencies remain distinct Fourier coordinates after lifting to one common modulus `Q`.

For the normalized `W`-local pair main at a booked source shift `h`, write

\[
g_{d,c}(h):=\widehat G_{W,h}(c/d),
\qquad
B_d(h):=
\sum_{\substack{c\bmod d\\(c,d)=1}}
|g_{d,c}(h)|^2.
\tag{2}
\]

WI-064 used (1) once, with one common refinement containing every retained conductor. The obstruction there was that Mikawa controls a residue **maximum**, so passing from the fine-modulus residue vector to his square-function budget costs the refinement modulus `Q`.

The natural remaining question is whether many smaller refinements can share the spectrum and average that `Q` cost away.

## 2. Allow arbitrary redundant linear refinement, not merely a partition

Fix any finite set `\mathcal Q` of **distinct** admissible refinement moduli in Mikawa's range

\[
Q\le Q_*.
\tag{3}
\]

Repeated copies of the same `Q` are not separate arithmetic information and are merged before the argument.

For every retained reduced frequency `(d,c)`, allow an arbitrary complex decomposition over all refinements containing that conductor:

\[
\boxed{
 g_{d,c}(h)
 =
 \sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
 g_{d,c;Q}(h).
}
\tag{4}
\]

This strictly contains the blockwise-partition escape stated in WI-064: a partition corresponds to assigning each `(d,c)` to exactly one `Q`, while (4) permits the same mode to be split redundantly among many refinements with arbitrary phases and amplitudes.

For one `Q`, define the coefficient energy

\[
A_Q(h)
:=
\sum_{\substack{d\mid Q\\(c,d)=1}}
|g_{d,c;Q}(h)|^2,
\tag{5}
\]

where the sum is only over the retained modes actually assigned to `Q`. By (1), the corresponding error contraction can be written entirely in distinct Fourier coordinates of the single fine-residue vector modulo `Q`:

\[
C_Q(k)
:=
\sum_{\substack{d\mid Q\\(c,d)=1}}
 g_{d,c;Q}(h_1(k))
 \widetilde T_{Q,cQ/d}(h_2(k)).
\tag{6}
\]

Exact Cauchy--Schwarz and Parseval give

\[
\boxed{
|C_Q(k)|^2
\le
A_Q(h_1(k))
Q\sum_{a\bmod Q}
|\widetilde E_Q(a,h_2(k))|^2.
}
\tag{7}
\]

Equation (4) implies that the reconstructed retained contraction is exactly

\[
C_{\rm ret}=\sum_{Q\in\mathcal Q}C_Q.
\tag{8}
\]

No triangle inequality has yet been used across conductors or refinement moduli.

## 3. Even an optimistic Mikawa splice gives block norm caps `(Q A_Q)(Q M_Q)`

Let

\[
A_Q^*:=\sup_k A_Q(h_1(k))
\tag{9}
\]

on the finite booked source family, and let

\[
M_Q
:=
\max_{(a,Q)=1}
\sum_H |E(X;Q,a,H)|^2
\tag{10}
\]

be the Mikawa residue-max pair-error square sum, with `X` denoting the ambient pair-count length in this finding.

The non-reduced classes in (7) have the separate prime-power treatment reconstructed in WI-061. For the present obstruction, grant that nuisance away completely and pretend that the full fine-residue norm costs no more than its reduced-residue contribution. This can only make the proposed repair easier. On the booked injective shift family one then has the optimistic estimate

\[
\begin{aligned}
\|C_Q\|_{\ell^2(k)}^2
&\le
A_Q^*\,Q\,\varphi(Q)M_Q\\
&\le
A_Q^*Q^2M_Q\\
&=
\boxed{(Q A_Q^*)(Q M_Q)}.
\end{aligned}
\tag{11}
\]

WI-061 extracts from Mikawa's proof, for every fixed `A>0` with the corresponding fixed modulus-range loss,

\[
\boxed{
\sum_{Q\le Q_*} Q M_Q
\ll_A X^3(\log X)^{-A}.
}
\tag{12}
\]

Because the moduli in `\mathcal Q` are distinct, the same budget applies to their subfamily.

Now apply the sharp Hilbert-space assembly lemma already proved in WI-062 to the vectors `C_Q`, with

\[
a_Q=Q A_Q^*,
\qquad
y_Q=Q M_Q.
\tag{13}
\]

Using only (11)--(12), the optimal universal estimate is

\[
\boxed{
\|C_{\rm ret}\|_2^2
\le
\left(\sum_{Q\in\mathcal Q}Q A_Q^*\right)
\left(\sum_{Q\in\mathcal Q}Q M_Q\right).
}
\tag{14}
\]

As in WI-062, the first coefficient cannot be improved from the block norm caps and the total arithmetic budget alone: abstract Hilbert vectors can saturate the Cauchy assembly. Any improvement after (11) must therefore use a genuine relation among different refinement blocks.

## 4. Redundant lifting can save at most one harmonic logarithm

Fix one booked full-active source shift `h_0`. Since `A_Q^*\ge A_Q(h_0)`, put

\[
S:=\sum_{Q\in\mathcal Q}Q A_Q^*.
\tag{15}
\]

Then

\[
S
\ge
\sum_{d,c}
\sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
Q|g_{d,c;Q}(h_0)|^2.
\tag{16}
\]

For one retained frequency, (4) and weighted Cauchy give

\[
\begin{aligned}
|g_{d,c}(h_0)|^2
&=
\left|
\sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
\sqrt Q\,g_{d,c;Q}(h_0)\,Q^{-1/2}
\right|^2\\
&\le
\left(
\sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
Q|g_{d,c;Q}(h_0)|^2
\right)
\left(
\sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
\frac1Q
\right).
\end{aligned}
\tag{17}
\]

Define

\[
H_d(\mathcal Q)
:=
\sum_{\substack{Q\in\mathcal Q\\d\mid Q}}
\frac1Q.
\tag{18}
\]

Even if **every** positive multiple of `d` up to `Q_*` were available,

\[
\begin{aligned}
H_d(\mathcal Q)
&\le
\sum_{1\le r\le Q_*/d}\frac1{dr}\\
&\le
\frac{1+\log(Q_*/d)}d\\
&\le
\frac{1+\log Q_*}{d}.
\end{aligned}
\tag{19}
\]

Squarefreeness, coprimality, parity, or a smaller admissible modulus family only decrease the left side, so (19) is deliberately maximally favorable to the redundant-refinement proposal.

Combining (17)--(19), summing primitive frequencies, and using (2) yields the exact lower bound

\[
\boxed{
S
\ge
\frac1{1+\log Q_*}
\sum_{d\in\mathcal D_{\rm ret}}
 d B_d(h_0).
}
\tag{20}
\]

This is the decisive point. One common refinement in WI-064 paid the full refinement modulus. A partition into many refinements cannot improve the diagonal cost at all beyond the choice of the `Q` attached to each conductor. Even arbitrary **redundant** splitting among all admissible multiples can reduce the diagonal conductor weight by at most the harmonic factor `1+log Q_*`.

The bound is phase-insensitive and allows arbitrary complex cancellation in (4). It is therefore not an artifact of assigning conductors disjointly.

## 5. WI-059 makes the lower bound super-polylogarithmic for every lossless retained spectrum

Assume that the retained exact-conductor family is asymptotically lossless for the chosen full-active shift `h_0`:

\[
\frac{
\sum_{d\in\mathcal D_{\rm ret}}B_d(h_0)
}{
\sum_dB_d(h_0)
}
\longrightarrow1.
\tag{21}
\]

Uniform losslessness over the source family is stronger than (21), so any source-uniform construction is covered.

WI-059 proves that for every **fixed** `K>0` there is `c_K>0` such that

\[
\liminf
\frac{
\sum_{d>w^K}B_d(h_0)
}{
\sum_dB_d(h_0)
}
\ge c_K,
\tag{22}
\]

and also

\[
\sum_dB_d(h_0)=\|G_{W,h_0}\|_2^2\gg\log w.
\tag{23}
\]

Therefore (21)--(23) imply, for each fixed `K` and all sufficiently large source scale,

\[
\begin{aligned}
\sum_{d\in\mathcal D_{\rm ret}}dB_d(h_0)
&\ge
w^K
\sum_{\substack{d\in\mathcal D_{\rm ret}\\d>w^K}}
B_d(h_0)\\
&\gg_K
w^K\log w.
\end{aligned}
\tag{24}
\]

At the source scale used in WI-059,

\[
w=(\log X)^C
\tag{25}
\]

with fixed `C>0`, while Mikawa's usable range has `Q_*\le X^{1/2}` up to a fixed logarithmic loss. Hence

\[
1+\log Q_*\ll\log X,
\tag{26}
\]

and (20), (24) give

\[
\boxed{
S
\gg_K
(\log X)^{CK-1}\log\log X.
}
\tag{27}
\]

Because `K` in WI-059 may be any fixed constant, for every fixed `A>0` choose `K>(A+1)/C`. Then

\[
\boxed{
\frac{S}{(\log X)^A}\longrightarrow\infty.
}
\tag{28}
\]

Thus the optimal coefficient available from the entire redundant-refinement architecture is still super-polylogarithmic. Mikawa supplies arbitrarily strong but **fixed** logarithmic savings, not a saving with exponent growing with `X`. No fixed choice of the exponent in (12) can absorb (28).

The explicit lossless cutoff from WI-059 is `X^{o(1)}`, so it remains far below Mikawa's square-root modulus range for every fixed logarithmic-saving parameter. The obstruction is not caused by running out of available refinement moduli; it is the residue-max/Hilbert information interface itself.

## 6. Stress tests and exact scope

Several possible loopholes do **not** invalidate the statement above.

1. **Using smaller blocks.** A disjoint partition is a special case of (4), so it is already included.
2. **Overlapping blocks.** A frequency may be split among arbitrarily many different multiples `Q`; (17)--(20) already optimize over that redundancy.
3. **Complex phases.** Equation (17) uses the exact reconstruction constraint and is valid for arbitrary complex coefficients.
4. **All multiples rather than squarefree admissible refinements.** Equation (19) intentionally grants all positive multiples. The true Yang/Mikawa admissible family can only have a smaller reciprocal sum and therefore a larger cost.
5. **Non-reduced residues.** They were granted away in (11). Restoring their prime-power contribution cannot make a norm-only upper-bound route easier.
6. **Shift-dependent decompositions.** The lower bound uses only one booked source shift `h_0` and `A_Q^*\ge A_Q(h_0)`. Allowing the coefficient split to vary with the booked shift does not evade (20) at that shift.

The finding deliberately does **not** rule out arguments using information absent from (11)--(12). In particular, it leaves alive:

- a residue-summed or genuinely vector-valued prime-pair dispersion theorem replacing Mikawa's `max_a` interface;
- cross-`Q` orthogonality/correlation strong enough to improve the sharp generic Hilbert assembly (14);
- a direct source-normalized covariance estimate that never scalarizes into refinement-block norms;
- a source-specific identity that reduces the required retained `W`-local spectrum before the lossless criterion (21) is imposed.

The conclusion is therefore an information-interface barrier, not a claim that the actual arithmetic covariance is large.

## 7. Prior-art and novelty audit

The mathematical ingredients in the lower bound are classical: weighted Cauchy--Schwarz, harmonic-series bounds, finite Fourier/Parseval lifting, and the general large-sieve/Bombieri--Vinogradov philosophy. No novelty is claimed for any of those ingredients or for interpreting repeated fine-modulus lifts as a redundant frame.

The arithmetic source remains H. Mikawa, *On prime twins in arithmetic progressions*, *Tsukuba J. Math.* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`, whose residue-max theorem and pre-Cauchy square-function step were reconstructed in WI-061. WI-064 supplies the source-specific exact divisor-martingale/Fourier consistency that makes redundant lifting legitimate. WI-059 supplies the exact `W`-local conductor-energy tail forcing any lossless retained family beyond every fixed polylogarithmic cutoff.

A targeted prior-art check around Barban--Davenport--Halberstam variance, prime-pair/progression mean values, Kawada's prime `k`-tuple progression theorem, large-sieve conductor decompositions, and vector-valued Bombieri--Vinogradov estimates did not locate an established theorem that gives the missing **residue-summed shifted-prime-pair** norm or a cross-refinement estimate stronger than the Mikawa information used here. Classical Barban--Davenport--Halberstam does sum squared errors over residues, but for the ordinary prime-counting error rather than Mikawa's shifted pair correlation, so it is not silently substituted into (11). Kawada's multiplet-in-progression work likewise does not provide, from the theorem surface audited here, the vector-valued pair-error estimate required to bypass (14).

Absence from this bounded search is **not** used as a priority claim. The durable Mathia contribution claimed here is only the exact source-specific narrowing: granting the WI-064 martingale structure and allowing arbitrary redundant common refinements still leaves a super-polylogarithmic cost unless one also imports genuinely new cross-refinement or residue-averaged arithmetic information.

## 8. Consequence for the research program

WI-064 left `blockwise common refinements` as its first positive escape. The present finding closes the entire version of that route in which each refinement is reduced to a norm cap of the form (11) and the refinement vectors are then assembled from only Mikawa's total budget (12). The stronger redundant model shows that this is not merely a bad partition choice.

The surviving target is correspondingly sharper:

\[
\boxed{
\text{the next useful input must act before the residue-max/block-norm scalarization,}
}
\]

for example through a residue-averaged/vector-valued shifted-pair theorem, a proved cross-refinement covariance law, or a direct estimate for the Yang contraction. Merely choosing more refinement blocks, overlapping them, or retuning the conductor partition remains inside the barrier.

## 9. Decisive audit / falsification gates

Narrow or withdraw the conclusion if any of the following occurs.

1. The exact refinement identity (1) from WI-064 fails under the final source parity/collision convention. The present argument otherwise uses only algebra after that identity.
2. The square-function extraction (12) from Mikawa's proof fails independent audit. In that case the algebraic lower bound (17)--(20) remains exact, but the claimed consequence for the present Mikawa repair must be downgraded with WI-061.
3. WI-059's positive fixed-`K` conductor-energy tail fails on the actual full-active source shift family. That would remove the super-polylogarithmic step (22)--(28).
4. An established arithmetic theorem controls the residue-summed/vector-valued shifted-prime-pair error before the `max_a` loss, or supplies a cross-refinement quadratic form not reducible to (11)--(12). That would not falsify the weighted-frame lower bound, but it would bypass the information interface this finding closes.
5. A proposed refinement scheme does not admit a reconstruction of the retained Fourier contraction in the form (4)--(8), and proves a genuinely different source identity rather than simply reweighting or duplicating the same reduced rational frequencies. Such a scheme lies outside the stated architecture and must be audited on its own terms.
