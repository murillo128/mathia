# MC-450 — LCM frequency synchronization recombines to the centered sieve autocorrelation

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-INGREDIENTS` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the incomplete translated-character branch of `MC-413` and the fixed-lcm Fourier analysis of `MC-446`--`MC-449`. Let `p` be prime, let `chi` be a nonprincipal multiplicative character modulo `p`, and fix a nonzero shift `h in F_p^*`. Put

\[
f_a(x):=\chi(x+a)\overline{\chi(x)},
\qquad
g_a(x):=f_a(x)+\frac1p.
\tag{1}
\]

For every unit `L mod p`, set

\[
a_L:=hL^{-1}\pmod p.
\tag{2}
\]

With the additive Fourier convention

\[
\widehat g_a(t):=\sum_{x\bmod p}g_a(x)e_p(-tx),
\qquad e_p(y):=e^{2\pi i y/p},
\tag{3}
\]

there is an exact dilation covariance

\[
\boxed{
\widehat g_{a_L}(mL)=\widehat g_h(m)
\qquad(m\bmod p).
}
\tag{4}
\]

Thus the lcm-dependent translated-character multipliers can indeed be synchronized: on the `L`-slice one may reindex the Fourier frequency as `t=mL`, after which every slice sees the same multiplier `\widehat g_h(m)`.

However, this synchronization creates **no new averaging variable**. Let a finite family of compatible divisor-pair pieces be indexed after CRT reduction by `(L,r)`, with `0<=r<L`, coefficient `c_{L,r}`, and a finite integer interval `I_{L,r}` of `k`-values. Define

\[
\mathcal C^\circ
:=\sum_{L,r}c_{L,r}
\sum_{k\in I_{L,r}}
 g_{a_L}(k+rL^{-1}).
\tag{5}
\]

Then `(4)` gives

\[
\boxed{
\mathcal C^\circ
=\frac1p\sum_{m\bmod p}\widehat g_h(m)B(m),
}
\tag{6}
\]

where

\[
B(m):=\sum_{L,r}c_{L,r}
\sum_{k\in I_{L,r}}e_p\!\bigl(m(r+Lk)\bigr).
\tag{7}
\]

If

\[
b_h(x):=
\sum_{\substack{L,r,k:\ k\in I_{L,r}\\r+Lk\equiv x\ (p)}}c_{L,r},
\qquad x\in F_p,
\tag{8}
\]

then

\[
B(m)=\widehat b_h(-m)
\tag{9}
\]

and therefore `(6)` is simply finite Fourier Parseval for

\[
\boxed{
\mathcal C^\circ=\sum_{x\bmod p}b_h(x)g_h(x).
}
\tag{10}
\]

For the actual upper-sieve autocorrelation of `MC-409`--`MC-413`, before any absolute values are taken, the divisor-pair expansion recombines pointwise to

\[
b(n)=w(n+h)w(n)\ge0,
\tag{11}
\]

and `(10)` is the residue-class aggregation of

\[
\sum_n b(n)g_h(n)
=\sum_n w(n+h)w(n)
\left(\chi(n+h)\overline{\chi(n)}+\frac1p\right).
\tag{12}
\]

In the divisor-pair coordinates, complete `p`-blocks of `g_{a_L}` vanish before the pieces are recombined. Equation `(12)` is the exact recombined form of that centered source-sensitive component, with the universal zero mode separated as in `MC-449`. Hence synchronizing the lcm slices by `t=mL` and then fully recombining them returns to the original centered additive-differenced correlation. It does not manufacture an extra cross-lcm source coordinate.

Moreover, generic Cauchy after this synchronization is **exactly the generic physical-space Cauchy bound**. Since

\[
\|g_h\|_2^2=p-2-\frac1p,
\tag{13}
\]

Parseval gives

\[
\frac1p\|\widehat g_h\|_2\|\widehat b_h\|_2
=\|g_h\|_2\|b_h\|_2
=\sqrt{p-2-1/p}\,\|b_h\|_2.
\tag{14}
\]

Thus a proposed cross-lcm argument that does nothing beyond the slice-wise reindexing `t=mL`, sums the resulting Fourier coefficients, and applies generic Cauchy has merely rewritten the same `L^2` estimate in dual coordinates. Any real cross-lcm gain must preserve and exploit additional structure **before** the divisor-pair/lcm pieces are recombined into `b_h`—for example well-factorable coefficient decomposition, a smaller dispersion diagonal, modulus factorization, or a nonuniform correlation between the actual source coefficients and the character multiplier.

A related fixed-lcm fact also rules out treating the bare CRT start set as automatically Fourier-flat. For one `L`, write

\[
W_L(u):=\sum_r c_{L,r}\,\mathbf 1_{u=rL^{-1}},
\qquad
A_L:=\sum_r c_{L,r},
\qquad
V_L:=\sum_r|c_{L,r}|.
\tag{15}
\]

Then

\[
\widehat W_L(-mL)=\sum_r c_{L,r}e_p(mr)
\tag{16}
\]

and, because `0<=r<L`,

\[
\boxed{
|\widehat W_L(-mL)-A_L|
\le \frac{2\pi |m|L}{p}\,V_L.
}
\tag{17}
\]

Consequently, whenever `|A_L|>=eta V_L`, all frequencies with

\[
|m|\le \frac{\eta p}{4\pi L}
\tag{18}
\]

satisfy

\[
|\widehat W_L(-mL)|\ge \frac\eta2 V_L.
\tag{19}
\]

For equal positive weights this gives a low-frequency resonant band of width on the order of `p/L`. Therefore the CRT-idempotent geometry by itself does not produce Fourier flatness in the conductor embedding. The only ways around `(17)` are coefficient cancellation in `A_L`, interaction with the interval factor, or genuinely nonuniform spectral structure; those are precisely additional arithmetic inputs, not consequences of support geometry alone.

No estimate for `M(x)`, a twisted Mertens sum, or an individual incomplete character sum follows.

## 1. Dilation covariance of the translated kernel

Equation `(4)` is elementary but load-bearing. For `a_L=hL^{-1}`, substitute `y=Lx` in `(3)`. Since `L` is a unit modulo `p`, this is a permutation of `F_p`, and

\[
\begin{aligned}
\widehat f_{a_L}(mL)
&=\sum_x
\chi(x+hL^{-1})\overline{\chi(x)}e_p(-mLx)\\
&=\sum_y
\chi(L^{-1}(y+h))\overline{\chi(L^{-1}y)}e_p(-my)\\
&=\sum_y
\chi(y+h)\overline{\chi(y)}e_p(-my)\\
&=\widehat f_h(m).
\end{aligned}
\tag{20}
\]

The scalar `chi(L^{-1})` cancels its conjugate. The centering constant in `(1)` is invariant under dilation, so the same identity holds for `g`, proving `(4)`.

This is the translated analogue of the Fourier equivariance already exposed for the bare product phase in `MC-411`, but the interpretation is different. Additive differencing has genuinely created a nonseparable translated character phase; `(4)` says only that the particular lcm dependence `a_L=h/L` is exactly the one removed by simultaneously dilating the start/frequency coordinate by `L`.

## 2. Cross-lcm synchronization is the inverse CRT change of variables

For one term of `(5)`, finite Fourier inversion gives

\[
g_{a_L}(k+rL^{-1})
=\frac1p\sum_{t\bmod p}
\widehat g_{a_L}(t)
 e_p\!\left(t(k+rL^{-1})\right).
\tag{21}
\]

Reindex `t=mL`. Using `(4)`, the right side becomes

\[
\frac1p\sum_m
\widehat g_h(m)e_p\!\bigl(m(Lk+r)\bigr).
\tag{22}
\]

Summing over `(L,r,k)` proves `(6)`--`(7)`. But `n=r+Lk` is exactly the original integer variable used before the CRT substitution in `MC-413`. Therefore `(7)` is just the additive Fourier transform of the recombined coefficient as stated in `(8)`--`(9)`.

The apparent common frequency `m` is not a new arithmetic coordinate. It is the ordinary Fourier frequency conjugate to the original variable `n`. The map

\[
(L,r,k,t)\longmapsto (n=r+Lk,\ m=tL^{-1})
\tag{23}
\]

is an invertible slice-wise reparameterization as long as `(L,p)=1`.

For the upper-sieve weight, expanding

\[
w(n+h)w(n)
=\sum_{d\mid n+h}\sum_{e\mid n}\lambda_d\lambda_e
\tag{24}
\]

and grouping by the corresponding CRT `(L,r)` gives exactly the coefficients in `(5)`. Thus full recombination yields `(11)`--`(12)`. For each divisor-pair progression, every complete `p`-block of `g_{a_L}` has zero sum before the pieces are recombined. Equation `(12)` therefore packages the same centered complete/incomplete separation without turning it into a new lcm variable.

## 3. Generic dual-space Cauchy cannot improve the recombined form

The function `f_h` has modulus one at every residue except `0` and `-h`, where one character factor vanishes. Hence

\[
\sum_x|f_h(x)|^2=p-2.
\tag{25}
\]

Also `sum_x f_h(x)=-1` by the complete correlation in `MC-448`. Therefore

\[
\begin{aligned}
\sum_x|g_h(x)|^2
&=\sum_x|f_h(x)|^2
+\frac{2}{p}\Re\sum_x f_h(x)
+\frac1p\\
&=p-2-\frac1p,
\end{aligned}
\tag{26}
\]

which proves `(13)`.

Applying Cauchy to `(6)` and Parseval to both factors gives `(14)`. Applying Cauchy directly to `(10)` gives exactly the same quantity. Thus the synchronized Fourier representation has no hidden `L^2` advantage. Any improvement must use a norm, decomposition, cancellation, or bilinear relation that is lost if the coefficient pieces are first summed into the single residue weight `b_h`.

For the actual upper sieve this distinction is sharp. The recombined weight in `(11)` is nonnegative, while the well-factorable components supplied by `MC-409` are signed convolutional objects. Their potential analytic value exists only before full recombination. A proof that first sums all lcm slices into `(11)` and only then invokes generic Fourier `L^2` has discarded the coefficient factorability it was supposed to exploit.

## 4. The fixed-lcm start set has a deterministic resonant band unless its coefficients cancel

Equation `(16)` follows immediately from the definition of `W_L` and the canonical CRT representative `0<=r<L` from `MC-447`. Using `|e^{i theta}-1|<=|theta|`,

\[
\begin{aligned}
|\widehat W_L(-mL)-A_L|
&\le\sum_r|c_{L,r}|\,|e_p(mr)-1|\\
&\le \frac{2\pi|m|}{p}\sum_r|c_{L,r}|r\\
&\le\frac{2\pi|m|L}{p}V_L,
\end{aligned}
\tag{27}
\]

proving `(17)`. Equations `(18)`--`(19)` follow by the reverse triangle inequality.

This is a representation-level obstruction, not a character-sum lower bound. The complete multiplier `\widehat g_h(m)` and the interval factor can still be small or oscillatory on this band, and the actual signed coefficients can make `A_L` small. What `(17)` rules out is the weaker hope that the Boolean CRT-idempotent support alone is sufficiently pseudorandom in the conductor Fourier coordinates to force a broad saving.

## 5. Prior art and novelty boundary

No new finite-field Fourier theorem is claimed. Dilation covariance of a Fourier transform under multiplication by a unit, Parseval, and the identity between a grouped sum and its recombination are elementary finite harmonic analysis. The mixed rational-character Fourier envelope used in the neighboring `MC-448` is classical and anchored by `MC-S55` (Cochrane--Pinner); it is not needed for the exact collapse `(4)`--`(14)`.

The relevant analytic comparison is the genuine `q`-van der Corput literature. Irving, *Estimates for Character Sums and Dirichlet L-Functions to Smooth Moduli* (IMRN 2016, DOI `10.1093/imrn/rnv285`, arXiv:`1503.07156`), obtains gains for smooth squarefree moduli by an `A`-process that uses a nontrivial factorization of the modulus before completion. That is structurally different from the invertible slice-wise dual reindexing `(23)`: the modulus factorization changes the arithmetic problem, whereas `(23)` only changes coordinates.

A targeted literature search on 22 September 2026 found the standard finite-Fourier equivariance and the established q-vdC/modulus-factorization framework, but no reason to assign independent novelty to `(4)` or `(6)`. The durable Mathia contribution is the branch-specific closure: the most immediate way of coupling many lcm slices in the Fourier representation—align their translated-character multipliers by `t=mL` and then apply generic `L^2`—is exactly the centered original correlation in dual coordinates and cannot itself lower the source-depth tariff.

## Boundaries and falsification tests

- **Prime conductor and invertible `L` are assumed.** Composite/smooth conductors can support genuine modulus factorization. Such a factorization before scalarization is outside the no-go and remains live.
- **The no-go is against synchronization plus generic recombination/Cauchy.** A dispersion identity that keeps well-factorable components separate and has a smaller diagonal is not equivalent to `(14)` and is not ruled out.
- **Variable interval lengths are allowed in `(5)`--`(9)`.** They are absorbed into the physical coefficient `b_h`; the exact reparameterization does not require a common `H`.
- **The positivity statement applies after full upper-sieve recombination.** Individual factorable components and incomplete CRT pieces can be signed. Their cancellation is precisely information that must be used before passing to `(11)`.
- **The resonant-band estimate concerns the start-set transform only.** It is not a lower bound for the full translated-character aggregate because the character multiplier and interval kernel may cancel it.
- **Small `A_L` is a genuine escape.** If the actual signed fixed-lcm coefficients have strong zero-mode cancellation, `(17)` permits Fourier flatness; proving and propagating that cancellation would be new arithmetic input rather than support geometry.
- **Modulus factorization remains live.** The exact q-vdC gains in the cited smooth-modulus literature use arithmetic factors of the conductor, not merely lcm-dependent frequency relabeling.
- **No RH input enters.** The argument is finite CRT algebra, centering, and Fourier analysis.

## Consequence for the research line

`MC-446`--`MC-449` closed ambient-box averaging, hidden frame multiplicity, one-fixed-lcm uniform Fourier envelopes, and the near-complete interval loophole. The simplest remaining cross-lcm repair is now closed as well: synchronizing the lcm-dependent shifts by `t=mL` exposes a common character multiplier, but after the slices are summed it is exactly the Fourier transform of the original centered additive-differenced sieve correlation. Generic dual `L^2` is therefore identical to generic physical `L^2`.

The accepted source-frame clue should now reserve **cross-lcm coupling** for a genuinely stronger mechanism: one that keeps factorable coefficient components or conductor factors visible long enough to change the diagonal/off-diagonal geometry before recombination. Detailed weighted CRT Fourier structure also remains live only insofar as it uses actual signed coefficients or multiplier correlation; the unweighted/start-set geometry alone has the resonant band `(17)` and is not automatically Fourier-flat.