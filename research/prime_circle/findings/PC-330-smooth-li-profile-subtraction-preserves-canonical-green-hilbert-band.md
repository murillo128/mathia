# PC-330 — smooth Li-profile subtraction preserves the canonical Green Hilbert band

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the full smooth-profile renormalization escape left by PC-328/PC-329.

PC-328 identifies a smooth PNT/Li low-frequency packet behind the escaping outliers of the canonical growing-conductor Green family, and PC-329 proves that no fixed finite packet or fixed-rank subtraction can remove that background. A natural next step is therefore to subtract the **entire** matched Li source profile rather than finitely many modes.

That subtraction does remove the smooth fixed-frequency packet, but it does **not** regularize the Green operator at its intrinsic Hilbert-band scale. The reason is exact and geometric: the normalized prime source is sparse, whereas the Li-grid control is diffuse. Their physical-space `L^2` distance is asymptotically the full prime-source `L^2` norm. By finite cyclic Parseval, almost all Fourier energy therefore survives the subtraction even though every fixed low Fourier mode is removed. When the residual is inserted into the canonical Green kernel, the universal Hilbert band from PC-323 survives with asymptotically unchanged scale.

There are two natural meanings of “subtract the full Li profile”, and both have the same obstruction:

1. **source-level subtraction:** replace the prime source by prime minus Li-grid source, then rebuild the Green operator; its Hilbert-band scale is asymptotic to the original one;
2. **operator-level subtraction:** subtract the complete Li-grid Green operator from the prime Green operator; the difference still has one dominant Hilbert channel of asymptotically the original scale.

Thus the full smooth Li profile can remove the PNT-driven low-mode outliers of PC-328, but it cannot by itself remove the noncompact canonical Green background. A viable continuation must additionally subtract or match the source's high-frequency sparse-energy Hilbert channel, or work with a genuinely relative invariant after that channel has been removed.

## 1. Prime and Li-grid sources on the conductor polygon

Let `q` be prime and let `P_q` be the canonical prime source set used in PC-277--PC-329, with

\[
R_q:=|P_q|\sim \frac q{\log q}.
\tag{1}
\]

On `Z/qZ`, write the prime probability vector

\[
p_q(j):=\frac{1}{R_q}\mathbf 1_{P_q}(j).
\tag{2}
\]

For nonzero frequencies define

\[
a_q(h):=\sum_{j\bmod q}p_q(j)e^{-2\pi i hj/q},
\qquad 1\le h\le q-1,
\tag{3}
\]

and set `a_q(0)=0` when viewing the centered periodic source as in PC-323/PC-328. Finite cyclic Parseval gives the exact RMS identity

\[
\boxed{
\mu_q^{P}
:=\frac1q\sum_{h=1}^{q-1}|a_q(h)|^2
=\frac1{R_q}-\frac1q
\sim\frac{\log q}{q}.
}
\tag{4}
\]

Now let `\widetilde\lambda_q` be the denominator-`q` Li-grid control from PC-277/PC-285: start with the normalized logarithmic-integral probability measure on `[2/q,1]` and project each point to a nearest denominator-`q` grid point. Let

\[
w_q(j):=\widetilde\lambda_q(\{j/q\})
\tag{5}
\]

and for `h\ne0`

\[
\ell_q(h):=\sum_{j\bmod q}w_q(j)e^{-2\pi i hj/q},
\qquad \ell_q(0):=0.
\tag{6}
\]

The control is diffuse in the precise `L^2` sense

\[
\boxed{
\|w_q\|_{\ell^2(\mathbb Z/q\mathbb Z)}^2=O(q^{-1}).
}
\tag{7}
\]

To see this directly, write

\[
A_q:=\operatorname{Li}(q)-\operatorname{Li}(2)\asymp \frac q{\log q}.
\]

In the normalized coordinate `t=x/q`, the continuous Li density is

\[
\varphi_q(t)=\frac{q}{A_q\log(qt)}.
\tag{8}
\]

On `t\ge q^{-1/2}`, one has `\varphi_q(t)=O(1)`, so every nearest-grid cell there has mass `O(1/q)` and contributes `O(1/q)` in total squared mass. On `2/q\le t<q^{-1/2}`, every cell has mass `O((\log q)/q)`, while the total mass of the whole interval is

\[
O\!\left(\frac{\operatorname{Li}(\sqrt q)}{\operatorname{Li}(q)}\right)
=O(q^{-1/2}).
\]

Hence its total squared cell mass is

\[
O\!\left(\frac{\log q}{q^{3/2}}\right)=o(q^{-1}),
\]

which proves (7). Parseval therefore gives

\[
\boxed{
\mu_q^{L}
:=\frac1q\sum_{h=1}^{q-1}|\ell_q(h)|^2
=\|w_q\|_2^2-\frac1q
=O(q^{-1}).
}
\tag{9}
\]

Thus the smooth Li control carries a factor `1/log q` less Fourier RMS energy than the sparse prime source:

\[
\boxed{
\frac{\mu_q^L}{\mu_q^P}=O\!\left(\frac1{\log q}\right).
}
\tag{10}
\]

## 2. Full source subtraction leaves asymptotically all RMS energy

Define the zero-mass physical residual

\[
d_q:=p_q-w_q
\tag{11}
\]

and its nonzero Fourier coefficients

\[
e_q(h):=a_q(h)-\ell_q(h).
\tag{12}
\]

Since `\sum_jd_q(j)=0`, Parseval is exact without a zero-mode correction:

\[
\mu_q^{\mathrm{res}}
:=\frac1q\sum_{h=1}^{q-1}|e_q(h)|^2
=\|d_q\|_2^2.
\tag{13}
\]

Expanding and using (7),

\[
\|d_q\|_2^2
=\frac1{R_q}+\|w_q\|_2^2
-2\langle p_q,w_q\rangle,
\tag{14}
\]

while Cauchy--Schwarz gives

\[
|\langle p_q,w_q\rangle|
\le \|p_q\|_2\|w_q\|_2
=O\!\left(\frac1{\sqrt{R_q q}}\right).
\tag{15}
\]

Because `R_q/q\asymp1/\log q`, equations (7), (14), and (15) imply

\[
\boxed{
\mu_q^{\mathrm{res}}
=\frac1{R_q}
\left(1+O((\log q)^{-1/2})\right)
\sim\frac{\log q}{q}.
}
\tag{16}
\]

Comparing with (4),

\[
\boxed{
\frac{\mu_q^{\mathrm{res}}}{\mu_q^P}\longrightarrow1.
}
\tag{17}
\]

This is the central obstruction. The full Li source is an excellent weak/smooth approximation to the normalized prime source, but it is not an `L^2` approximation to the sparse source vector. Smooth subtraction therefore removes essentially none of the finite-cyclic Fourier energy.

At the same time it **does** remove the fixed low modes responsible for PC-328. Indeed, for every fixed integer `h`, the test `t\mapsto e^{-2\pi iht}` has Lipschitz constant `2\pi|h|`, so PC-285 gives

\[
\boxed{
|e_q(h)|
\ll_h
(\log q)e^{-cV(q)}+\frac{\log q}{q},
\qquad
V(q)=\frac{(\log q)^{3/5}}{(\log\log q)^{1/5}}.
}
\tag{18}
\]

By contrast PC-328 has

\[
a_q(h)=\frac{C_h}{\log q}+O_h((\log q)^{-2}),
\qquad C_h\ne0.
\tag{19}
\]

So (18) kills every fixed PNT/Li Fourier outlier while (16) says the total Fourier energy remains asymptotically unchanged. The subtraction does not eliminate the energy; it forces it into growing/high-frequency modes. This is a source-level effect before any spectral wrapper is chosen.

## 3. Rebuilding the Green operator from the residual preserves the band

For distinct prime conductors `q,r`, form the source-residual Green kernel

\[
X^{\mathrm{res}}_{q,r}(k,l)
:=\frac{e_q(k)e_r(l)}{k+l},
\qquad k,l\ge1,
\tag{20}
\]

with `e_q,e_r` extended periodically. Because a nonzero zero-mean sequence of prime period has exact period `q`, PC-323 applies directly. Its unique Hilbert-channel scale is

\[
c^{\mathrm{res}}_{q,r}
=\sqrt{\mu_q^{\mathrm{res}}\mu_r^{\mathrm{res}}}.
\tag{21}
\]

For the raw prime Green kernel the corresponding scale is

\[
c^{P}_{q,r}
=\sqrt{\mu_q^{P}\mu_r^{P}}.
\tag{22}
\]

Equation (17) therefore gives

\[
\boxed{
\frac{c^{\mathrm{res}}_{q,r}}{c^{P}_{q,r}}\longrightarrow1
\qquad(q,r\to\infty).
}
\tag{23}
\]

Hence the self-adjoint dilation of (20) still has

\[
\boxed{
\sigma_{\mathrm{ess}}
=
[-\pi c^{\mathrm{res}}_{q,r},\pi c^{\mathrm{res}}_{q,r}],
}
\tag{24}
\]

an essential Hilbert band of asymptotically the same width as the unrenormalized canonical prime operator. Moreover PC-327 applies again to this residual periodic source: after normalizing by `c^{res}_{q,r}`, its generalized-Hilbert offset defect still has the same universal logarithmic Schatten divergence. Full smooth source subtraction therefore does not make the Green family compact or uniformly Schatten-controlled.

## 4. Subtracting the complete Li Green operator also leaves one dominant band

A second natural interpretation is to keep the prime source unchanged but subtract the complete Green operator generated by the Li control. Write

\[
X^P_{q,r}=D_{a_q}K_1D_{a_r},
\qquad
X^L_{q,r}=D_{\ell_q}K_1D_{\ell_r},
\tag{25}
\]

where `(K_1)_{kl}=1/(k+l)`. PC-323 gives, after grouping by the common period `qr`,

\[
X^P_{q,r}=A_P\otimes H_1+S_P,
\qquad
X^L_{q,r}=A_L\otimes H_1+S_L,
\qquad S_P,S_L\in\mathcal S_1,
\tag{26}
\]

with rank-one channel norms

\[
\|A_P\|=c^P_{q,r},
\qquad
\|A_L\|=c^L_{q,r}:=\sqrt{\mu_q^L\mu_r^L}.
\tag{27}
\]

By (4) and (9),

\[
\boxed{
\frac{c^L_{q,r}}{c^P_{q,r}}
=O\!\left(\frac1{\sqrt{\log q\log r}}\right)
\longrightarrow0.
}
\tag{28}
\]

The complete operator difference is therefore

\[
X^P_{q,r}-X^L_{q,r}
=(A_P-A_L)\otimes H_1+(S_P-S_L).
\tag{29}
\]

Let `s_1>=s_2` be the singular values of the finite matrix `A_P-A_L`. The triangle inequality and the rank-one approximation bound give

\[
c^P_{q,r}-c^L_{q,r}
\le s_1\le
c^P_{q,r}+c^L_{q,r},
\tag{30}
\]

and

\[
s_2\le c^L_{q,r}.
\tag{31}
\]

Consequently

\[
\boxed{
\frac{s_1}{c^P_{q,r}}\to1,
\qquad
\frac{s_2}{c^P_{q,r}}\to0.
}
\tag{32}
\]

The self-adjoint dilation of the **fully Li-subtracted Green operator** therefore still has one dominant Hilbert branch whose band edge is

\[
\boxed{
\pi s_1
=\pi c^P_{q,r}(1+o(1)).
}
\tag{33}
\]

The smooth control can cancel the large low-frequency trace-class outliers of PC-328 while contributing asymptotically too little RMS channel energy to cancel the noncompact Hilbert core. Operator-level full-profile subtraction is therefore no more a complete renormalization than source-level subtraction.

## 5. Matched-control and novelty audit

The mechanism is not a new theorem in harmonic analysis or operator theory. The finite cyclic Parseval identity used in (4), (9), and (13) is standard. The Hilbert-matrix spectral facts and the generalized-Hilbert trace-class reduction in (24)--(33) are exactly the classical Magnus--Rosenblum/Kato--Rosenblum framework already anchored by PC-323. The PNT/Li transport in (18) is the classical source estimate already audited and strengthened in PC-277/PC-285.

A targeted external search against periodically weighted Hilbert/Hankel matrices, finite Fourier energy of sparse measures, and prime exponential sums found these expected classical ingredients but no independent statement combining the denominator-`q` Li control with the Prime-Circle Green renormalization. Contemporary work on prime exponential sums studies cancellation and mean-square phenomena rather than this deterministic sparse-versus-diffuse Parseval obstruction. No external theorem beyond the already-persisted ingredients is load-bearing here, so `SOURCES.md` does not need a new dependency.

The project-local delta is the renormalization boundary itself. PC-329 leaves a whole source-derived smooth profile as the natural escape from fixed-complexity deflation. Equations (17), (23), and (32) show that the obvious full Li implementation removes the smooth low-mode packet but **cannot remove the canonical Hilbert band**. This is stronger than saying that finitely many modes are insufficient: even the complete smooth profile has asymptotically negligible channel energy compared with the sparse prime source.

A matched non-prime control with comparable sparse `L^2` energy could evade this theorem. In particular, a random or deterministic sparse control with cardinality comparable to `R_q` can have `\mu\asymp\log q/q`, unlike the Li-grid control. Such controls are therefore mandatory falsification tests for any future claim based on the residual Hilbert band itself.

## 6. What this closes and what remains open

This finding closes the two direct continuations

\[
\text{prime source}-\text{smooth Li source}
\longrightarrow
\text{Green lift}
\longrightarrow
\text{bounded/compact residual family},
\tag{34}
\]

and

\[
\text{prime Green operator}-\text{Li Green operator}
\longrightarrow
\text{removal of the canonical Hilbert core}.
\tag{35}
\]

Both fail at the same RMS-energy gate. The smooth profile is strong enough to remove fixed PNT/Li Fourier structure and too diffuse to cancel the sparse-source Hilbert channel.

The theorem does **not** rule out the more demanding combined renormalization suggested by PC-323/PC-327: subtract the source-specific universal Hilbert channel itself, then subtract or compare the smooth Li low-frequency profile inside the remaining relative/trace-class data. It also does not classify a control deliberately engineered to match the prime source's full autocorrelation or sparse Fourier energy, nor does it provide a destination theorem connecting the surviving relative divisor to Riemann zeros.

The live Green frontier is therefore narrower. A future zero-sensitive claim must survive **both** controls simultaneously:

- removal of the universal source-energy Hilbert channel, and
- removal of the complete smooth PNT/Li profile.

Only the residual after both operations can legitimately be tested for a nonclassical divisor, sign law, compact spectral limit, or critical-line constraint. A subtraction that performs only the second operation remains noncompact for the elementary Parseval reason above.

## Audit tests

The claim is falsified if any of the following fails:

1. the chosen PC-277 nearest-grid Li control violates `\|w_q\|_2^2=O(1/q)`;
2. cyclic Parseval fails to give (4), (9), or (13) with the stated normalization;
3. `\|p_q-w_q\|_2^2/(1/R_q)` does not tend to `1`;
4. a fixed Fourier mode of the residual fails the PC-285 bounded-Lipschitz estimate (18);
5. applying the PC-323 residue decomposition to `e_q,e_r` gives a Hilbert scale not equal to (21);
6. the dominant singular value of `A_P-A_L` violates (30)--(32).

Passing these tests establishes only the full-smooth-profile no-go above. It does not establish RH, a zeta-zero spectral realization, or a lower bound for more sophisticated matched-energy renormalizations.