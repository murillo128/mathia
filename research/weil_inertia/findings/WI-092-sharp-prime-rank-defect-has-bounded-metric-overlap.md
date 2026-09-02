# WI-092 — Sharp prime Ramanujan rank defect has uniformly bounded metric overlap

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It adds metric information to the exact rank geometry of WI-087--WI-091. The close opposite-residue prime pairs that can lose asymptotically one third of the smaller Ramanujan rank are nevertheless weakly coupled after whitening: throughout the whole WI-091 triangular boundary layer, the squared canonical correlations have total mass strictly below `4`, independently of the prime sizes. Consequently only `O(1)` principal directions can have any fixed nonzero correlation, even though the cross Gram has rank `asymp p`. Combined with WI-091's fixed-window bounded-incidence theorem, near-one-third rank-defect edges cannot by themselves create extensive Hilbert--Schmidt cancellation in the signed scalar Ramanujan operator.

Let `p<q<2p` be distinct odd primes in opposite nonzero residue classes modulo `3`, let

\[
U_p^{(N)}=(e(ax/p))_{0\le x<N,\ 1\le a<p},
\qquad
U_q^{(N)}=(e(bx/q))_{0\le x<N,\ 1\le b<q},
\tag{1}
\]

and put

\[
H_p=(U_p^{(N)})^*U_p^{(N)},
\qquad
H_q=(U_q^{(N)})^*U_q^{(N)}.
\tag{2}
\]

In WI-091's genuinely residual regime these matrices are positive definite. Write

\[
\Pi_p=U_p^{(N)}H_p^{-1}(U_p^{(N)})^*,
\qquad
\Pi_q=U_q^{(N)}H_q^{-1}(U_q^{(N)})^*
\tag{3}
\]

for the orthogonal projectors onto the two sampled Ramanujan subspaces, and

\[
B_p=U_p^{(N)}(U_p^{(N)})^*,
\qquad
B_q=U_q^{(N)}(U_q^{(N)})^*
\tag{4}
\]

for the unwhitened positive blocks used in WI-079--WI-082.

Use WI-091's notation

\[
r=\frac{2p-q}{3},
\qquad
\beta=\frac{p+q}{3}=p-r,
\tag{5}
\]

and its canonical nearest-boundary length

\[
\delta_c=
\begin{cases}
(pq+p-q)/3,&p\equiv2,\ q\equiv1\pmod3,\\
(pq+q-p)/3,&p\equiv1,\ q\equiv2\pmod3.
\end{cases}
\tag{6}
\]

Assume

\[
\boxed{
\delta_N(p,q)=\delta_c+e,
\qquad |e|\le r-1.
}
\tag{7}
\]

Then the following metric bounds hold uniformly in the observation length `N`:

\[
\boxed{
\operatorname{tr}(\Pi_p\Pi_q)<4.
}
\tag{8}
\]

If `sigma_1,...,sigma_k` are the nonzero canonical correlations between the two sampled subspaces, then WI-091 gives

\[
k=\operatorname{rank}((U_p^{(N)})^*U_q^{(N)})=\beta+|e|,
\tag{9}
\]

while (8) gives

\[
\boxed{
\sum_{j=1}^{k}\sigma_j^2<4,
\qquad
\frac1k\sum_{j=1}^{k}\sigma_j^2
<\frac4{\beta+|e|}<\frac6p.
}
\tag{10}
\]

In particular, for every fixed `eta>0`,

\[
\boxed{
\#\{j:\sigma_j\ge\eta\}<\frac4{\eta^2}.
}
\tag{11}
\]

Thus the exact one-third rank obstruction is **not** a one-third family of strongly aligned directions. Its nonzero coupling rank grows linearly with `p`, but its total whitened squared overlap stays bounded.

The same statement has an unwhitened Hilbert--Schmidt form directly adapted to the positive blocks `B_p,B_q`:

\[
\boxed{
\frac{\operatorname{tr}(B_pB_q)}
{\|B_p\|_F\,\|B_q\|_F}
<
\frac4{\sqrt{(p-1)(q-1)}}
<\frac4{p-1}.
}
\tag{12}
\]

So a pair may have the maximum possible residual **rank** defect from WI-088 while its normalized Frobenius coherence tends to zero.

## 1. Finite-window projector overlap is a whitened cross-Gram norm

Set

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)}.
\tag{13}
\]

From (3), cyclicity of trace gives the exact identity

\[
\begin{aligned}
\operatorname{tr}(\Pi_p\Pi_q)
&=
\operatorname{tr}
\left(
H_p^{-1}G_{p,q}^{(N)}H_q^{-1}(G_{p,q}^{(N)})^*
\right)\\
&=
\left\|
H_p^{-1/2}G_{p,q}^{(N)}H_q^{-1/2}
\right\|_F^2.
\end{aligned}
\tag{14}
\]

The singular values in (14) are the canonical correlations between the two column spaces, so (14) is also the classical principal-angle identity

\[
\operatorname{tr}(\Pi_p\Pi_q)=\sum_j\cos^2\theta_j.
\tag{15}
\]

No arithmetic input enters (14)--(15). The arithmetic content below is the uniform bound on this standard subspace metric for the special WI-091 boundary family.

## 2. Exact Frobenius energy of a prime-pair boundary cross Gram

WI-081 proves that complete `pq` periods contribute zero to the cross Gram and that passing from the retained boundary of length `r_N=N mod pq` to its complement only introduces an overall sign and diagonal unitary phase factors. Hence, with

\[
\delta=\delta_N(p,q),
\tag{16}
\]

one has the **metric**, not merely rank, equality

\[
\boxed{
\|G_{p,q}^{(N)}\|_F
=
\|G_{p,q}^{(\delta)}\|_F.
}
\tag{17}
\]

For `0<delta<pq`, write

\[
A=\left\lfloor\frac{\delta-1}{p}\right\rfloor,
\qquad
C=\left\lfloor\frac{\delta-1}{q}\right\rfloor.
\tag{18}
\]

The Gram-entry expansion and the prime Ramanujan formula give

\[
\begin{aligned}
\|G_{p,q}^{(\delta)}\|_F^2
&=
\sum_{|h|<\delta}(\delta-|h|)c_p(h)c_q(h).
\end{aligned}
\tag{19}
\]

For prime `p`,

\[
c_p(h)=
\begin{cases}
p-1,&p\mid h,\\-1,&p\nmid h.
\end{cases}
\tag{20}
\]

Since no nonzero `|h|<delta<pq` is divisible by both primes, use the constant baseline `c_p(h)c_q(h)=1`. The total triangular weight is

\[
\sum_{|h|<\delta}(\delta-|h|)=\delta^2.
\tag{21}
\]

At `h=0` the correction from the baseline is `pq-p-q`; at every nonzero multiple of `p` the correction is `-p`; at every nonzero multiple of `q` it is `-q`. Summing the arithmetic progressions yields the exact closed form

\[
\boxed{
\begin{aligned}
F_{p,q}(\delta)
:=\|G_{p,q}^{(\delta)}\|_F^2
={}&\delta^2+\delta(pq-p-q)\\
&-2pA\delta+p^2A(A+1)\\
&-2qC\delta+q^2C(C+1).
\end{aligned}
}
\tag{22}
\]

This formula is useful independently of the later estimate: it gives the exact squared cross-block energy for every prime pair and every nearest-boundary length below one full pair period.

## 3. Each sampled prime block has an exact residue-count frame lower bound

Let

\[
a_p=\left\lfloor\frac Np\right\rfloor.
\tag{23}
\]

Among `N` consecutive sample positions, each residue modulo `p` occurs either `a_p` or `a_p+1` times. For every coefficient vector `v in C^(p-1)`, group the samples by residue and use the `p`-point Fourier orthogonality of the nonzero frequency columns:

\[
\begin{aligned}
\|U_p^{(N)}v\|_2^2
&=\sum_{x\bmod p}n_x
\left|\sum_{a=1}^{p-1}v_a e(ax/p)\right|^2\\
&\ge a_p
\sum_{x\bmod p}
\left|\sum_{a=1}^{p-1}v_a e(ax/p)\right|^2\\
&=p a_p\|v\|_2^2.
\end{aligned}
\tag{24}
\]

Therefore

\[
\boxed{
H_p\succeq p\left\lfloor\frac Np\right\rfloor I,
\qquad
H_q\succeq q\left\lfloor\frac Nq\right\rfloor I.
}
\tag{25}
\]

Combining (14), (17) and (25), and using `N>=delta`, gives

\[
\boxed{
\operatorname{tr}(\Pi_p\Pi_q)
\le
\frac{F_{p,q}(\delta)}
{p\lfloor\delta/p\rfloor\ q\lfloor\delta/q\rfloor}
}
\tag{26}
\]

whenever the two displayed floors are positive. They are positive throughout the WI-091 residual layer.

The same lower frame bound gives

\[
\|B_p\|_F^2
=\operatorname{tr}(H_p^2)
\ge
(p-1)
\left(p\left\lfloor\frac Np\right\rfloor\right)^2,
\tag{27}
\]

and analogously for `q`. Since

\[
\operatorname{tr}(B_pB_q)=\|G_{p,q}^{(N)}\|_F^2,
\tag{28}
\]

equations (22), (25) and (27) will convert the same scalar estimate into (12).

## 4. The whole WI-091 triangular layer satisfies the uniform constant `4`

There are two residue orientations. The proof is elementary but the endpoint arithmetic matters because the result must hold for every shift `e` in the exact triangular layer, not only at its apex.

### Orientation `p=3a+2`, `q=3b+1`

The prime inequalities `p<q<2p` give

\[
a\ge1,
\qquad
a+1\le b\le2a.
\tag{29}
\]

Here

\[
r=2a-b+1,
\qquad
|e|\le2a-b,
\tag{30}
\]

and

\[
\delta
=\delta_c+e
=3ab+2a+b+1+e.
\tag{31}
\]

Direct division gives

\[
\delta-bp=r+e\in[1,2r-1]\subset[1,p-1],
\tag{32}
\]

and

\[
0<a+b+1+e=\delta-aq<q.
\tag{33}
\]

Hence

\[
\boxed{
\left\lfloor\frac\delta p\right\rfloor=b,
\qquad
\left\lfloor\frac\delta q\right\rfloor=a.
}
\tag{34}
\]

In particular `A=b` and `C=a` in (22). After substituting (31), the dependence on `e` is

\[
F_{p,q}(\delta)
=e^2+(3ab+2a+b+1)e+\text{constant}.
\tag{35}
\]

Its forward difference is

\[
F(e+1)-F(e)
=2e+3ab+2a+b+2.
\tag{36}
\]

At the left endpoint `e=b-2a`, the right-hand side is

\[
3ab-2a+3b+2>0,
\]

so `F` is increasing throughout the allowed integer interval. Its maximum is therefore at `e=2a-b`. At that endpoint exact expansion gives

\[
\begin{aligned}
4pqab-F
={}&18a^2b^2-9a^2b-9a^2
+6ab^2-6ab-3a\\
&-4b^2-3b.
\end{aligned}
\tag{37}
\]

To prove positivity without any numerical case split, discard the positive term `6ab^2`. The remaining leading term obeys

\[
9a^2b(2b-1)
\ge9a^2(a+1)(2a+1),
\tag{38}
\]

while `b<=2a` gives

\[
9a^2+6ab+3a+4b^2+3b
\le37a^2+9a.
\tag{39}
\]

The difference of the right sides in (38)--(39) is

\[
a\left[8+(a-1)(18a^2+45a+17)\right]>0.
\tag{40}
\]

Therefore

\[
F_{p,q}(\delta)<4pqab
\tag{41}
\]

throughout this orientation.

### Orientation `p=3a+1`, `q=3b+2`

Now `p` is an odd prime greater than `3`, so `a>=2`, and

\[
a\le b\le2a-1.
\tag{42}
\]

One has

\[
r=2a-b,
\qquad
|e|\le2a-b-1,
\tag{43}
\]

and

\[
\delta
=3ab+a+2b+1+e.
\tag{44}
\]

Again direct division gives

\[
\boxed{
\left\lfloor\frac\delta p\right\rfloor=b,
\qquad
\left\lfloor\frac\delta q\right\rfloor=a.
}
\tag{45}
\]

Here the `e`-dependent part of (22) is

\[
e^2+(3ab+a+2b+1)e,
\tag{46}
\]

whose forward difference is positive throughout (43); at the left endpoint it is already

\[
3ab-3a+4b+4>0.
\tag{47}
\]

Thus the maximum again occurs at the positive endpoint `e=2a-b-1`. Exact expansion now factors cleanly:

\[
\boxed{
4pqab-F
=a\left(18ab^2-3ab-10a-6b-1\right).
}
\tag{48}
\]

Since `b>=a` and `b<=2a-1`, the bracket is at least

\[
3a^2(6a-1)-(22a-5)
=93+(a-2)(18a^2+33a+44)>0.
\tag{49}
\]

Hence (41) holds in the mirror orientation as well.

Equations (26), (34), (41) and (45) prove (8).

## 5. Rank is large while every fixed-strength principal-angle population is bounded

For full-column-rank `U_p,U_q`, multiplication by `H_p^{-1/2}` and `H_q^{-1/2}` does not change cross-Gram rank. Therefore the number of nonzero canonical correlations in (14) equals

\[
\operatorname{rank}G_{p,q}^{(N)}.
\tag{50}
\]

WI-091 proves that this rank is exactly `beta+|e|` in the triangular layer. Combining (8), (14) and (50) gives the first inequality in (10). Since `q>p`,

\[
\beta=\frac{p+q}{3}>\frac{2p}{3},
\tag{51}
\]

which gives the second inequality in (10). Finally, if `M_eta` canonical correlations are at least `eta`, then

\[
M_\eta\eta^2
\le\sum_j\sigma_j^2<4,
\tag{52}
\]

proving (11).

This is the key distinction from the rank-only picture. The WI-087/WI-088 obstruction says that roughly two thirds of the smaller frequency directions can remain coupled after roughly one third disappear. Equation (11) says that among those surviving directions, only a bounded number can remain coupled at any fixed order-one strength.

## 6. The unwhitened Ramanujan blocks have vanishing normalized Frobenius coherence

From (27)--(28),

\[
\begin{aligned}
\frac{\operatorname{tr}(B_pB_q)}
{\|B_p\|_F\|B_q\|_F}
&\le
\frac{F_{p,q}(\delta)}
{pq\lfloor N/p\rfloor\lfloor N/q\rfloor
\sqrt{(p-1)(q-1)}}\\
&\le
\frac{F_{p,q}(\delta)}
{pqab\sqrt{(p-1)(q-1)}}\\
&<\frac4{\sqrt{(p-1)(q-1)}},
\end{aligned}
\tag{53}
\]

which is (12). Thus the metric weakness is not an artifact of whitening. It is already visible in the original positive Gram blocks once each block is normalized by its own Hilbert--Schmidt energy.

There is a useful fixed-window consequence when (53) is combined with WI-091's incidence theorem. Fix an integer `D>=0`. Let `E_D(N;P)` be any graph of residual close-prime pairs `p<q`, with all endpoints at least `P`, satisfying WI-091's near-ceiling assumptions

\[
\tau_{p,q}(\delta_N)
\ge C_3(2p-q)-D
\tag{54}
\]

and

\[
D<
\left\lfloor\frac{2p-q}{3}\right\rfloor
-
\left\lfloor\frac{2p-q}{4}\right\rfloor.
\tag{55}
\]

WI-091 then forces every such edge into the triangular layer and gives

\[
\Delta(E_D)\le8D+4.
\tag{56}
\]

For arbitrary real block weights `omega_p`, set

\[
x_p=|\omega_p|\,\|B_p\|_F.
\tag{57}
\]

The absolute Hilbert--Schmidt cross contribution of just these near-ceiling edges is bounded by

\[
\begin{aligned}
\left|
2\sum_{\{p,q\}\in E_D}
\omega_p\omega_q\operatorname{tr}(B_pB_q)
\right|
&<
\frac8{P-1}
\sum_{\{p,q\}\in E_D}x_px_q\\
&\le
\frac4{P-1}
\sum_p\deg_{E_D}(p)x_p^2\\
&\le
\boxed{
\frac{4(8D+4)}{P-1}\sum_p x_p^2.
}
\end{aligned}
\tag{58}
\]

The quantity `sum_p x_p^2` is exactly the diagonal-block contribution to

\[
\left\|\sum_p\omega_p B_p\right\|_F^2.
\tag{59}
\]

Therefore, for fixed `D`, the near-one-third defect family contributes only `O(D/P)` of the diagonal Hilbert--Schmidt mass as the prime scale grows. For the exact ceiling `D=0`, WI-090's sharper matching theorem gives degree at most `1`, improving the coefficient in (58) from `16/(P-1)` to `4/(P-1)`.

Equation (58) is deliberately a statement about the designated near-ceiling edge family. Other prime pairs can contribute cross terms of either sign. It would be invalid to drop them and infer a lower bound for the full signed operator without controlling those remaining interactions.

## 7. Stress tests and failure boundaries

The load-bearing restrictions are explicit.

1. **Residual regime.** The projectors in (3) use invertible `H_p,H_q`. WI-091's triangular layer lies beyond both primitive-frequency dimensions, so `N>=delta>q-1` and both sampled Vandermonde blocks have full column rank.
2. **Nearest-boundary complement.** WI-081's shorter-side reduction preserves Frobenius norm because the complementary segment is a translated consecutive block and the translation acts by diagonal unitary phases. The proof does not silently replace a rank equality by a metric equality.
3. **Prime hypothesis.** Formula (20) and the two-floor arithmetic in section 4 are prime-specific. Composite Ramanujan spaces need a different divisor decomposition and are not covered by (8).
4. **Triangular layer.** A bounded-overlap statement of this strength is not asserted for every residual prime boundary. Near the first residual scale `delta just above q`, the crude projector-overlap bound can be much larger. The theorem targets exactly the family responsible for WI-088's asymptotically sharp one-third rank loss.
5. **The constant `4` is not claimed sharp.** It is a clean universal rational envelope obtained from the exact Frobenius formula and the residue-count frame lower bound. No numerical optimization is used in the proof.
6. **Rank and metric are different invariants.** Equation (8) does not improve WI-091's rank theorem; it shows why a large rank defect should not be interpreted as large metric cancellation.
7. **No Yang source-interface theorem is supplied.** WI-079--WI-082 remain conditional on a source-faithful scalar signed Ramanujan reduction of the post-local-main Yang covariance. This finding constrains that interface if used; it does not prove that the full covariance has this form.
8. **Moderate-defect pairs remain live.** Equation (58) closes the possibility that the *near-maximal one-third rank-defect family by itself* carries extensive Hilbert--Schmidt cancellation. It does not rule out accumulation from the much larger population of pairs with weaker rank defect or from genuinely labelled/two-dimensional source structure.

Direct floating-point projector checks on small triangular examples were used only as falsifiers during derivation; they are not evidence for (8). The exact proof is equations (17)--(49).

## 8. Prior art and novelty boundary

The ambient harmonic and matrix geometry is classical.

- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals** and **Part II: FIR Representations and Applications**, *IEEE Transactions on Signal Processing* 62 (2014), develop Ramanujan subspaces, finite-duration representations and orthogonal projections. These sources are already anchored in `research/weil_inertia/SOURCES.md` for WI-080.
- Vaidyanathan and Srikanth Tenneti, **Ramanujan subspaces and digital signal processing**, 48th Asilomar Conference on Signals, Systems and Computers (2014), explicitly emphasizes near-orthogonal bases for Ramanujan spaces. This is direct conceptual prior art for asking about finite-duration metric overlap.
- Principal angles/canonical correlations, the identity `tr(PQ)=sum cos^2 theta_j`, Vandermonde/DFT frame bounds, and Hilbert--Schmidt coherence are classical finite-dimensional linear algebra and harmonic analysis. No novelty is claimed for those mechanisms.
- WI-080 supplies complete-period Ramanujan orthogonality, WI-081 supplies the exact nearest-LCM boundary factorization, and WI-087--WI-091 supply the sharp close-prime rank-defect family and its fixed-`N` incidence geometry.

A targeted search across finite-duration Ramanujan subspaces, near-orthogonal Ramanujan bases, subspace principal angles, projector overlap, finite-window cross correlation and roots-of-unity Fourier subspaces located the general signal-processing framework above but did not locate the exact prime-pair estimate (8), the arithmetic triangular-layer specialization (34)--(49), or the fixed-window consequence (58). This is **not** a priority claim. The durable result is the exact consequence derived here from the persisted prime boundary geometry and classical subspace identities.

## 9. Consequence for the research program

WI-088 showed that residual prime pairwise rank loss can really reach one third, so a route based on proving every cross Gram almost full rank is impossible. WI-091 then showed that near-maximal defect is arithmetically confined to a triangular boundary layer and has bounded incidence at fixed observation length. The present result adds the missing metric statement:

\[
\boxed{
\text{one-third rank defect}
\quad\not\Rightarrow\quad
\text{order-one metric alignment on one-third of the modes};
}
\tag{60}
\]

instead,

\[
\boxed{
\sum_j\sigma_j^2<4
\quad\text{while}\quad
\#\{j:\sigma_j>0\}=\beta+|e|\asymp p.
}
\tag{61}
\]

Together with the fixed-`N` degree bound, the strongest pairwise rank obstructions are too sparse and too weak in normalized Hilbert--Schmidt geometry to be the sole source of an extensive signed scalar cancellation. This removes one pessimistic assembly model left open after WI-082: **macroscopic pairwise rank defect cannot simply be converted into macroscopic metric cancellation edge by edge.**

The live scalar problem is correspondingly narrower. Any large cancellation must come from the accumulated metric geometry of the much broader moderate-defect family, from coefficient-dependent singular-value structure beyond the uniform estimates here, or from information discarded by scalarization. That is the level at which a future repair of the Yang locked covariance must now be tested.