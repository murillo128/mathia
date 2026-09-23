# MC-475 — Pair-sieve Parseval coupling pays the full frequency dimension

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-474` left a specific possible escape from the exponential Fourier `ell^1` cost: the centered pair-sieve mask has small Fourier `ell^2` energy, so perhaps Cauchy--Schwarz, Parseval, or an ordinary additive large-sieve estimate could couple the mask to the translated-ratio character sums before modewise absolute values.

For the exact hard pair sieve, that **plain Hilbert-space escape does not buy cancellation**. The dual response energy can be evaluated exactly, and in the live incomplete regime it pays the full `W`-dimensional Fourier grid.

Keep the notation of `MC-472`--`MC-474`. Let `p` be prime, `chi` a nonprincipal character modulo `p`,

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\qquad h\not\equiv0\pmod p,
\tag{1}
\]

and let `W` be square-free with `(W,p)=1`. Put

\[
A(a)=A_{W,h}(a)=\mathbf 1_{(a(a+h),W)=1},
\qquad
\delta=\delta_W(h)=\frac1W\sum_{a\bmod W}A(a),
\tag{2}
\]

and center the mask by

\[
B(a)=A(a)-\delta.
\tag{3}
\]

Use the normalized Fourier transform

\[
\widehat B(r)=\frac1W\sum_{a\bmod W}B(a)e_W(-ra).
\tag{4}
\]

Then `widehat B(0)=0` and, as already recorded in `MC-474`,

\[
\sum_{r\bmod W}|\widehat B(r)|^2
=\delta(1-\delta).
\tag{5}
\]

For an interval `I` define the twisted responses

\[
S_r(I)=\sum_{n\in I}K_h(n)e_W(rn).
\tag{6}
\]

Fourier inversion gives the exact centered pairing

\[
E_{W,h}(I)
:=\sum_{n\in I}K_h(n)B(n)
=
\sum_{r\ne0\bmod W}\widehat B(r)S_r(I).
\tag{7}
\]

The natural Cauchy--Schwarz step therefore reads

\[
|E_{W,h}(I)|^2
\le
\delta(1-\delta)
\sum_{r\ne0\bmod W}|S_r(I)|^2.
\tag{8}
\]

The second factor is not mysterious. Group the interval by residue classes modulo `W`:

\[
F_a(I):=
\sum_{\substack{n\in I\\ n\equiv a\pmod W}}K_h(n).
\tag{9}
\]

Since

\[
S_r(I)=\sum_{a\bmod W}F_a(I)e_W(ra),
\tag{10}
\]

finite Parseval gives the exact identity

\[
\boxed{
\sum_{r\bmod W}|S_r(I)|^2
=W\sum_{a\bmod W}|F_a(I)|^2.
}
\tag{11}
\]

Removing the zero mode yields

\[
\boxed{
\sum_{r\ne0\bmod W}|S_r(I)|^2
=
W\sum_{a\bmod W}|F_a(I)|^2
-
\left|\sum_{n\in I}K_h(n)\right|^2.
}
\tag{12}
\]

Thus the proposed Fourier `ell^2` rescue is exactly a **residue-class second-moment problem modulo the full primorial modulus `W`**. It does not compress the frequency dimension.

This becomes decisive in the live sparse-interval regime. Let `H=|I|`. If

\[
H<W,
\tag{13}
\]

then each residue class modulo `W` contains at most one point of `I`, so

\[
\sum_{a\bmod W}|F_a(I)|^2
=
\sum_{n\in I}|K_h(n)|^2.
\tag{14}
\]

If also `H<=p`, then `K_h(n)` has modulus `1` except when `n=0` or `n=-h (mod p)`. Hence

\[
\sum_{n\in I}|K_h(n)|^2=H-Z_I,
\qquad 0\le Z_I\le2,
\tag{15}
\]

and consequently

\[
\boxed{
\sum_{r\ne0}|S_r(I)|^2
=W(H-Z_I)-|S_0(I)|^2.
}
\tag{16}
\]

For example, if `H>=4` and `W>=4H`, the trivial bound `|S_0(I)|<=H` gives

\[
\frac14WH
\le
\sum_{r\ne0}|S_r(I)|^2
\le WH.
\tag{17}
\]

So the dual response vector has norm of order `sqrt(W H)` before any arithmetic refinement. Combining `(5)` and `(17)`, the norm envelope in the direct Cauchy--Parseval proof is of order

\[
\sqrt{\delta(1-\delta)WH}.
\tag{18}
\]

For a surviving primorial pair sieve with `z>2`, the shift is even and the local factor at `2` is `1/2`, hence `delta<=1/2`. Conversely the factors with `q|h` are larger than the generic factors, so Mertens' theorem gives the coarse uniform lower scale

\[
\delta_W(h)
\gg
\prod_{3\le q<z}\left(1-\frac2q\right)
\asymp
\frac1{(\log z)^2}
\tag{19}
\]

up to an absolute constant and the harmless omission of `p` from `W`. Therefore, when `z` is a fixed positive power of `p`,

\[
W=W_z=\exp((1+o(1))z)
\tag{20}
\]

is superpolynomial in `p`, while `delta` loses only polylogarithmically. In the live `H<=p` range the Cauchy--Parseval envelope `(18)` is then vastly larger than the trivial `O(H)` scale.

This is **not a lower bound for the true pairing** `E_{W,h}(I)`. It says something narrower and methodologically useful: the small `ell^2` Fourier norm of the centered sieve mask does not by itself produce a useful estimate, because the matching full-grid response energy carries the entire primorial frequency dimension.

The incomplete discrepancy from `MC-472` is

\[
\mathcal D_{W,h}(I)
=
E_{W,h}(I)
+
\delta\left(S_0(I)+\frac Hp\right).
\tag{21}
\]

The present obstruction concerns the centered term `E`. It does not alter the separate zero-mode term in `(21)` and does not estimate the discrepancy itself.

## 1. The `ell^2` gain in `MC-474` is real but mismatched

Equation `(5)` is genuinely small: unlike the exponentially large Fourier `ell^1` norm in `MC-474`, the centered pair mask has total Fourier energy at most `1/4`. The failed step is not Parseval on the mask. It is the assumption that this low mask energy can be paired with a response vector whose energy is also independent of `W`.

Identity `(12)` shows exactly where the missing dimension reappears. The `W` additive frequencies are an orthogonal basis for functions on `Z/WZ`; summing all twisted responses over that basis simply measures the residue-class energy of the interval sequence. When `H<W`, the interval occupies distinct residue classes, so orthogonality reproduces essentially `W H` with no possibility of frequency-side averaging gain.

Equivalently, the exact Fourier expansion has embedded an `H`-point interval into a `W`-dimensional dual frame. Cauchy--Schwarz sees the norm of that full frame, not the small number of occupied physical points.

## 2. Ordinary additive large sieve reproduces the same obstruction

The classical large sieve treats a trigonometric polynomial evaluated at well-spaced frequencies. On the complete grid

\[
\left\{\frac rW:0\le r<W\right\},
\tag{22}
\]

the spacing is exactly `1/W`. The standard additive large-sieve scale for an interval of length `H` is therefore

\[
H+W.
\tag{23}
\]

When `W>>H`, the `W` term dominates. In the present complete-grid situation `(11)` is sharper than invoking a general inequality: it is an equality, and `(16)` shows that the `W` term is genuinely saturated in the sparse-interval regime.

Thus replacing the direct Cauchy--Parseval calculation by an **ordinary full-grid additive large sieve cannot remove the primorial-dimensional cost**. Any useful large-sieve-type escape must exploit additional structure that changes the effective family, weights the frequencies nontrivially, or couples the sieve and character before the complete `W`-grid response is formed.

## 3. This is distinct from the earlier `L2` barriers

The line already contains other Parseval and second-moment obstructions, notably `MC-263`, `MC-272`, and `MC-280`. They concern different objects: exceptional blind relations in a shell family, Cauchy norms of a positive generating polynomial, and low-degree Walsh decoders respectively.

The present identity is tied to the concrete `MC-472` pair-sieve discrepancy and closes the particular `ell^2` Fourier escape explicitly left open by `MC-474`. Its content is the exact duality

\[
\text{full additive-mode energy}
=
W\times\text{residue-class energy},
\tag{24}
\]

followed by the observation that the live interval is sparse modulo `W`. No general claim is made that `ell^2` methods are useless elsewhere in the research line.

## 4. Prior-art and novelty boundary

The mathematical ingredients in `(5)`, `(11)`, and `(12)` are classical finite Fourier analysis and Parseval. The comparison in §2 is the classical large-sieve geometry of a trigonometric polynomial sampled at well-spaced points. A modern reference is H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory II: Primes and Sieves*, Chapter 19, “The Large Sieve,” Cambridge University Press, 2026, DOI `10.1017/9781009445030.005`, which takes the trigonometric mean-square form as the fundamental large-sieve formulation. No new large-sieve theorem is claimed.

The important surviving boundary is also classical. Ben Green and Terence Tao, *Restriction theory of the Selberg sieve, with applications*, Journal de Théorie des Nombres de Bordeaux 18 (2006), no. 1, 147--182, DOI `10.5802/jtnb.538`, prove an `L^2`--`L^p` restriction theorem for Selberg-sieve majorants. That result is not asserted to apply to the exact shifted pair mask and translated-ratio character phase here. It matters because it demonstrates that **structured restriction estimates are genuinely stronger objects than the plain full-grid `ell^2` estimate closed above**.

A targeted audit on 23 September 2026 found no basis for a novelty claim for Parseval, the full-grid large-sieve comparison, or sieve restriction theory. The durable line-specific result is their exact specialization to the live pair-sieve response: the cheap mask `ell^2` norm is canceled by a full-dimensional dual-response norm before any conductor-power saving appears.

## Boundaries and falsification tests

- **No lower bound for `E` or `mathcal D` is proved.** Equations `(16)`--`(18)` diagnose the size of the Cauchy--Schwarz norm envelope, not the signed inner product.
- **The sparse formula uses `H<W`; the clean `Z_I<=2` statement also uses `H<=p`.** Outside that range, `(12)` remains exact but the residue-class energy must be analyzed rather than replaced by `(15)`.
- **Restriction theory remains open.** Weighted `L^2`--`L^p` estimates, sieve-majorant restriction, sparse-frequency selection, or other non-Hilbertian control may exploit information discarded by plain Cauchy--Schwarz.
- **Bilinear and dispersion routes remain open.** A method that couples divisor/sieve structure to the character before expanding into all `W` additive modes is not subject to the full-grid calculation in this form.
- **Compressed sieve weights remain open.** Truncated beta-sieve, Buchstab, well-factorable, or other approximating weights can have a smaller effective spectral family, provided their approximation error is charged at conductor-power precision.
- **Boundary, nonempty, and cross-component channels remain separate.** The claim concerns only the centered rough×rough hard-mask component identified in `MC-471`.
- **Physical-space Cauchy is not an escape either, but it is not the theorem here.** It merely gives a trivial-scale estimate. The substantive point is why the apparently promising small Fourier `ell^2` energy from `MC-474` does not improve that scale under the obvious joint Hilbert-space pairing.

## Consequence for the research line

The exact hard-mask route is now classified through three successive scalarizations. `MC-473` shows that full divisor inclusion-exclusion plus branchwise completion pays exponential branch multiplicity. `MC-474` shows that exact Fourier expansion plus modewise absolute values pays an exponential Fourier `ell^1` norm. The present result shows that switching to **plain full-grid `ell^2` coupling** removes the exponential coefficient norm but immediately restores the enormous primorial dimension in the response energy.

Therefore the live rough×rough question is narrower than “try a large sieve.” A viable next theorem must be structurally stronger than ordinary Hilbert-space averaging over all additive modes: a sieve-specific restriction estimate, a weighted/sparse spectral theorem, or a bilinear/dispersion decomposition that avoids creating the full `W`-frequency frame before cancellation is used.

No conductor-power gain, bound for `M(x)`, zero-free region, or RH consequence is obtained.