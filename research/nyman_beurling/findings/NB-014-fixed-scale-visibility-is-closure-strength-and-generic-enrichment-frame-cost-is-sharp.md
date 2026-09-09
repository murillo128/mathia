# NB-014 — fixed-scale semigroup visibility is closure-strength and the generic enrichment frame cost is sharp

**Status:** `EXACT-DERIVED + TARGET-AWARE-ENRICHMENT + CLOSURE-STRENGTH-VISIBILITY-THRESHOLD + LCM-FRAME-SATURATION + NEGATIVE/METHOD-BOUNDARY`. `NB-010` forces a positive amount of finite semigroup defect whenever the Nyman distance stays above an explicit fixed-scale threshold. The proposed visible-defect clue supplies the exact conversion from the part of that defect seen by the old section to the actual decrement `d_N^2-d_{MN}^2`. Combining the two gives a sharp calibration: a merely positive visibility fraction at arbitrarily large **fixed** probe depths would already force the discrete Nyman distance to zero, hence prove RH. At the same time, the obvious hope that the frame denominator in that conversion is generically much smaller than `M-1` fails exactly on a broad lcm regime.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\]

and for the Bagchi dilation isometries put

\[
D_m=A_m^*-m^{-1/2}I,
\qquad
\mathcal E_M(r_N)=\sum_{m=2}^M\|D_mr_N\|^2.
\]

Define the section-visible defect and its frame operator by

\[
\mathcal J_{N,M}
:=\sum_{m=2}^M\|P_ND_mr_N\|^2,
\qquad
F_{N,M}:=\sum_{m=2}^M A_mP_NA_m^*.
\tag{1}
\]

For every even `M>=4`, write

\[
s_M:=\log2-\frac1M>0,
\qquad
b_M:=\frac1{\sqrt M\,s_M}.
\tag{2}
\]

Then the following two statements hold.

1. If for one fixed even `M` there are `eta_M>0` and `N_0` such that

\[
\mathcal J_{N,M}\ge\eta_M\mathcal E_M(r_N)
\qquad(N\ge N_0),
\tag{3}
\]

then the monotone limit

\[
d_\infty:=\lim_{N\to\infty}d_N
\]

satisfies

\[
\boxed{d_\infty\le b_M.}
\tag{4}
\]

Consequently, if (3) can be proved for an unbounded sequence of fixed even `M` values, with an arbitrary positive constant `eta_M` allowed to depend on `M`, then `d_\infty=0`; by the Báez--Duarte discrete Nyman criterion this is RH.

2. Let

\[
L_M:=\operatorname{lcm}(2,3,\ldots,M).
\]

Whenever `L_M<=N`,

\[
\boxed{\|F_{N,M}\|=M-1.}
\tag{5}
\]

Thus the crude frame loss in the visible-defect conversion is the exact full operator norm throughout that regime. Since `\log L_M=\psi(M)\sim M`, for every fixed `epsilon>0` and all sufficiently large `N`, (5) holds uniformly for `M<=(1-epsilon)\log N`.

These results do not show that the actual residual has a useful visible fraction, nor that the frame compressed to the genuinely new quotient `V_{MN}\ominus V_N` has norm `M-1`. They show instead that two apparently mild shortcuts are unavailable: an `N`-uniform positive fixed-scale visibility theorem is already closure-strength, while an unconditional improvement of the **full** frame denominator is impossible in the lcm-overlap chamber. A viable continuation must therefore be scale-coupled and source-specific.

## 1. The exact visible-defect conversion

The dilation identity from the clue is immediate from the fractional-part generators:

\[
\boxed{A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m).}
\tag{6}
\]

Hence `A_mV_N subset V_{mN}`. Because `A_m` is an isometry, each

\[
Q_{m,N}:=A_mP_NA_m^*
\]

is the orthogonal projection onto `A_mV_N`, and therefore

\[
0\preceq F_{N,M}=\sum_{m=2}^M Q_{m,N}\preceq(M-1)I.
\tag{7}
\]

Also `P_Nr_N=0`, so the scalar term in `D_m` disappears after projection and

\[
\mathcal J_{N,M}
=\langle r_N,F_{N,M}r_N\rangle.
\tag{8}
\]

Since the range of `F_{N,M}` lies in `V_{MN}`, put

\[
u_{N,M}:=P_{MN}r_N=r_N-r_{MN}.
\]

Nested orthogonal projections give

\[
\|u_{N,M}\|^2=d_N^2-d_{MN}^2,
\tag{9}
\]

and (8) becomes

\[
\mathcal J_{N,M}
=\langle u_{N,M},F_{N,M}u_{N,M}\rangle.
\]

Therefore

\[
\boxed{
\mathcal J_{N,M}
\le\|F_{N,M}\|\,(d_N^2-d_{MN}^2)
\le(M-1)(d_N^2-d_{MN}^2).
}
\tag{10}
\]

This independently verifies the proposed clue's finite transport identity. It is an exact statement about the actual section spaces, not a Gram-only surrogate.

## 2. Fixed-scale positive visibility already bounds the limiting Nyman distance

`NB-010` proves, for every even `M>=4`,

\[
\boxed{
\mathcal E_M(r_N)
\ge
\frac{
\left[
 d_N^2\left(\log2-\frac1M\right)
 -\frac{d_N}{\sqrt M}
\right]_+^2
}{H_M-1}.
}
\tag{11}
\]

Assume (3). Combining (3), (10), and (11) yields

\[
d_N^2-d_{MN}^2
\ge
\frac{\eta_M}{(M-1)(H_M-1)}
\left[d_N^2s_M-\frac{d_N}{\sqrt M}\right]_+^2.
\tag{12}
\]

The sequence `d_N` is nonincreasing, so `d_N->d_infinity`; consequently both `d_N` and `d_(MN)` have the same limit and

\[
d_N^2-d_{MN}^2\longrightarrow0.
\tag{13}
\]

If `d_infinity>b_M`, then

\[
d_\infty^2s_M-\frac{d_\infty}{\sqrt M}>0,
\]

so the right side of (12) tends to a strictly positive constant, contradicting (13). This proves (4).

The contrapositive is a useful diagnostic. If `d_infinity>b_M`, then (10)--(11) imply, for all sufficiently large `N`,

\[
\boxed{
\frac{\mathcal J_{N,M}}{\mathcal E_M(r_N)}
\le
\frac{(M-1)(H_M-1)(d_N^2-d_{MN}^2)}
{\left(d_N^2s_M-d_N/\sqrt M\right)^2}
\longrightarrow0.
}
\tag{14}
\]

Thus under any nonzero limiting residual, fixed-scale visibility must collapse once `M` lies beyond the explicit threshold determined by that residual. The clue's conditional limit warning is therefore quantitative: an `N`-uniform positive visibility constant at fixed depth is not a harmless frame estimate; for unbounded depths it is already an RH proof mechanism.

## 3. Lcm overlap makes the full frame norm exactly maximal

Set `L=L_M` and assume `L<=N`. For every `2<=m<=M`, `m` divides `L`. Let

\[
Q:=\left\lfloor\frac{2N}{L}\right\rfloor\ge2.
\]

For `2<=q<=Q`, equation (6) gives

\[
A_{L/m}g_q
=\sqrt{L/m}\left(g_{(L/m)q}-q^{-1}g_{L/m}\right).
\]

Because `m>=2`,

\[
(L/m)q\le LQ/2\le N,
\]

and `L/m<=N`; hence `A_(L/m)g_q in V_N`. The semigroup law now gives

\[
A_Lg_q=A_mA_{L/m}g_q\in A_mV_N
\qquad(2\le m\le M).
\tag{15}
\]

Therefore

\[
\boxed{
A_LV_Q\subseteq\bigcap_{m=2}^M A_mV_N.
}
\tag{16}
\]

Every projection `Q_(m,N)` acts as the identity on this nonzero common subspace, so `F_(N,M)` acts there by the scalar `M-1`. Together with (7), this proves (5).

The common overlap is not merely an artifact of directions already contained in `V_N`. The generators `g_2,g_3,...` are linearly independent. Indeed, if

\[
\sum_{j=2}^K a_jg_j=0,
\]

then on the harmonic intervals the value sequence satisfies `sum_j a_j {n/j}=0`. Taking the difference between `n` and `n-1` gives

\[
\sum_{j=2}^K\frac{a_j}{j}
-\sum_{\substack{j\mid n\\2\le j\le K}}a_j=0.
\tag{17}
\]

For a prime `n>K` the divisor sum is empty, so the first term is zero. Setting successively `n=2,3,...,K` then gives `a_n=0` by induction over proper divisors.

Now put

\[
R=\left\lfloor\frac NL\right\rfloor,
\qquad q_0=R+1.
\]

Since `N/L>=1`, `q_0<=floor(2N/L)=Q`. Equation (15) shows `A_Lg_(q_0)` belongs to every `A_mV_N`, while

\[
A_Lg_{q_0}
=\sqrt L\left(g_{Lq_0}-q_0^{-1}g_L\right),
\qquad Lq_0>N.
\tag{18}
\]

Linear independence and `L<=N` imply

\[
A_Lg_{q_0}\notin V_N.
\tag{19}
\]

So the maximal common range has a genuinely new algebraic quotient direction. This still does **not** prove that the orthogonal compression of `F_(N,M)` to `V_N^perp` has norm `M-1`: subtracting the old projection of a common vector need not leave it inside every dilation range. Any useful improvement must therefore control those metric angles or work directly with the residual rather than infer them from range multiplicity.

Finally, the prime number theorem gives

\[
\log L_M=\psi(M)=M+o(M),
\tag{20}
\]

so the condition `L_M<=N` holds throughout every fixed sublogarithmic corridor `M<=(1-epsilon)log N` for sufficiently large `N`.

## 4. Prior-art boundary and research consequence

The external ingredients are already canonical in this line: Báez--Duarte supplies the discrete Nyman criterion, Bagchi supplies the integer-dilation Hilbert-space model, and the standard prime number theorem supplies (20), already used in `NB-008` for lcm growth. The visibility implication (12)--(14) uses only the exact section identity above and the locally derived `NB-010` parity bound.

A targeted literature check over Nyman--Beurling finite sections, Bagchi's dilation semigroup, dilation-frame/Galerkin enrichment, and lcm overlap did not locate this particular fixed-scale visibility threshold or the frame saturation (16). Recent work on multiscale Nyman Gram structure and general probabilistic/dilation variants concerns different approximation or Gram questions. Search absence is not evidence of novelty, and no external theorem beyond the existing source anchors is load-bearing here; `SOURCES.md` therefore does not change.

The line's next conversion problem is now more precise. A theorem of the form `J_(N,M)>=eta_M E_M` with `eta_M>0` uniformly in `N` cannot be pursued for arbitrarily large fixed `M` as a supposedly modest intermediate lemma: success would already close the discrete criterion. At the same time, replacing the denominator `M-1` by the full frame norm buys nothing whenever `lcm(2,...,M)<=N`.

The remaining nontrivial route is an **N-dependent** source estimate at a declared scale `M=M(N)` (or a direct section-decrement estimate) together with the residual-relevant compressed frame geometry on `V_(MN)\ominus V_N`. Such an estimate must be summed without assuming density of the trial spaces. Failure of fixed-scale uniform visibility does not refute this scale-coupled route, and (5) does not rule out a smaller compressed frame norm. No improved Nyman distance rate or RH conclusion is claimed here.