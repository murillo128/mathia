# MC-472 — Pair-sieve complete period factorizes

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The rough×rough pair-sieve channel isolated in `MC-471` has an exact complete-period factorization. This removes another possible source of hidden arithmetic resonance: on a complete joint period, the small-prime pair sieve and the translated-ratio character phase are independent CRT coordinates, so the sieve contributes only its ordinary local survivor density.

Let `p` be prime, let `chi` be a nonprincipal character modulo `p`, and let

\[
K_h(n):=\chi(n+h)\overline{\chi(n)},
\qquad h\not\equiv0\pmod p.
\tag{1}
\]

For any square-free `W` with `(W,p)=1`, define

\[
A_{W,h}(n):=\mathbf 1_{(n(n+h),W)=1}
\tag{2}
\]

and

\[
V_W(h):=\sum_{b\bmod W}A_{W,h}(b).
\tag{3}
\]

Then

\[
\boxed{
V_W(h)=\prod_{q\mid W}\bigl(q-\nu_q(h)\bigr),
}
\qquad
\nu_q(h):=\#\{0,-h\pmod q\}
=
\begin{cases}
1,&q\mid h,\\
2,&q\nmid h.
\end{cases}
\tag{4}
\]

and the complete joint-period character sum is exactly

\[
\boxed{
\sum_{n\bmod pW}K_h(n)A_{W,h}(n)
=-V_W(h).
}
\tag{5}
\]

Equivalently, with the pair-sieve density

\[
\delta_W(h):=\frac{V_W(h)}{W}
=\prod_{q\mid W}\left(1-\frac{\nu_q(h)}q\right),
\tag{6}
\]

the normalized complete mean is

\[
\boxed{
\frac1{pW}\sum_{n\bmod pW}K_h(n)A_{W,h}(n)
=-\frac{\delta_W(h)}p.
}
\tag{7}
\]

Thus the complete mean is exactly the complete mean `-1/p` of the translated-ratio character phase multiplied by the ordinary pair-sieve density. There is no additional complete-period character-versus-sieve cancellation or amplification to harvest.

For the actual rough factor of `MC-471`, put

\[
P(z)=\prod_{q<z}q,
\qquad
W_z:=\prod_{\substack{q<z\\q\ne p}}q.
\tag{8}
\]

If `p<z`, omitting `p` from the sieve in `(8)` does not change the weighted rough×rough sum, because `K_h(n)=0` whenever `p|n(n+h)`. Hence

\[
K_h(n)R_z(n)R_z(n+h)
=K_h(n)A_{W_z,h}(n)
\tag{9}
\]

for every `n`, so `(5)`--`(7)` apply without needing to assume `z<p`.

There are two immediate structural consequences.

First, because a nonprincipal character modulo a prime requires `p>2`, if `z>2` then `2|W_z`. For every odd shift `h`, the two forbidden classes `0,-h (mod 2)` exhaust both residues. Therefore

\[
\boxed{
h\ \text{odd},\ z>2
\quad\Longrightarrow\quad
R_z(n)R_z(n+h)=0\ \text{for every }n,
}
\tag{10}
\]

and the entire rough×rough channel vanishes exactly on odd shifts. The surviving rough×rough problem is an even-shift problem. This is only a constant-scale pruning of the shift family, not a conductor-power saving.

Second, the shift-average of the local density is also exact:

\[
\boxed{
\frac1W\sum_{h\bmod W}\delta_W(h)
=\left(\frac{\varphi(W)}W\right)^2.
}
\tag{11}
\]

So the `q|h` local degeneracies redistribute pair-sieve mass among shifts but do not increase its mean density above the independent two-unit baseline.

The unresolved arithmetic target is therefore not a complete-period local bias. It is the **incomplete joint-period discrepancy**. For an interval `I`, define

\[
\mathcal D_{W,h}(I)
:=
\sum_{n\in I}K_h(n)A_{W,h}(n)
+\frac{|I|}{p}\delta_W(h).
\tag{12}
\]

Then

\[
\sum_{n\in I}K_h(n)A_{W,h}(n)
=-\frac{|I|}{p}\delta_W(h)+\mathcal D_{W,h}(I).
\tag{13}
\]

The discrepancy in `(12)`, not the complete mean, is where any source-budget conductor-power gain must now occur. Complete-period blocking gives no nontrivial estimate in a genuinely incomplete regime: the joint period is `pW`, and a block argument only becomes useful once the interval is long compared with that period.

No estimate for `\mathcal D_{W,h}(I)` is proved here, and none is inferred from `(5)`.

## 1. Exact local survivor count

For a prime `q|W`, the condition

\[
q\nmid n(n+h)
\tag{14}
\]

removes the residue classes

\[
n\equiv0,-h\pmod q.
\tag{15}
\]

If `q\nmid h`, the two classes are distinct and there are `q-2` survivors. If `q|h`, they coincide and there are `q-1` survivors. Because `W` is square-free, the Chinese remainder theorem multiplies these local counts, proving `(4)`.

This also identifies `V_W(h)` as the cyclic autocorrelation of the reduced-residue indicator:

\[
V_W(h)
=
\sum_{b\bmod W}
\mathbf 1_{(b,W)=1}
\mathbf 1_{(b+h,W)=1}.
\tag{16}
\]

Thus the local `q|h` enhancement is the standard shifted pair-sieve/singular-series effect, not a new phase interaction.

The parity gate `(10)` is the `q=2` specialization. If `2|W` and `h` is odd, `q-2=0`; no pair survives. If `h` is even, the two forbidden classes coincide and the local factor is `1`.

## 2. Complete translated-ratio correlation is exactly `-1`

For `h not\equiv0 (mod p)`, extend `chi` by zero at `0`. The complete character correlation is

\[
S_p(h):=
\sum_{a\bmod p}\chi(a+h)\overline{\chi(a)}.
\tag{17}
\]

Only `a\ne0,-h` contribute. On this set,

\[
\chi(a+h)\overline{\chi(a)}
=
\chi\!\left(\frac{a+h}{a}\right).
\tag{18}
\]

The map

\[
a\longmapsto t=1+\frac ha
\tag{19}
\]

is a bijection from `F_p\setminus\{0,-h\}` to `F_p^\times\setminus\{1\}`. Therefore

\[
S_p(h)
=
\sum_{t\in\mathbb F_p^\times\setminus\{1\}}\chi(t)
=-1,
\tag{20}
\]

because a nonprincipal multiplicative character sums to zero on `F_p^\times` and `chi(1)=1`.

This is a classical complete-character identity; no novelty is claimed for `(20)`.

## 3. CRT makes the complete sieve/phase interaction a tensor product

Because `(p,W)=1`, a residue `n (mod pW)` corresponds independently to

\[
(a,b)\in\mathbb Z/p\mathbb Z\times\mathbb Z/W\mathbb Z.
\tag{21}
\]

The phase `K_h(n)` depends only on `a`, while `A_{W,h}(n)` depends only on `b`. Consequently

\[
\begin{aligned}
\sum_{n\bmod pW}K_h(n)A_{W,h}(n)
&=
\left(\sum_{a\bmod p}K_h(a)\right)
\left(\sum_{b\bmod W}A_{W,h}(b)\right)\\
&=(-1)V_W(h),
\end{aligned}
\tag{22}
\]

which proves `(5)`.

This exact tensor product is the main obstruction. A complete-period treatment cannot reveal a special resonance between rational-character oscillation modulo `p` and the small-prime pair sieve: those coordinates are literally independent under CRT. Any method that produces only complete sums plus a local sieve density has already used all the information available at that level.

For an interval of length `H`, periodic blocking leaves at most one residual segment shorter than `pW`. From `|K_hA_{W,h}|\le1`, this gives only a remainder of order `pW` (or the trivial order `H` when `H<pW`). Hence `(22)` by itself cannot solve the source-scale incomplete problem.

## 4. The shift-average degeneracy is exactly neutral

Summing `(16)` over `h (mod W)` gives a second CRT-free proof of `(11)`. Each ordered pair of reduced residues `(b,c)` determines exactly one shift

\[
h\equiv c-b\pmod W.
\tag{23}
\]

There are `phi(W)^2` such pairs, so

\[
\sum_{h\bmod W}V_W(h)=\varphi(W)^2.
\tag{24}
\]

Dividing by `W^2` yields `(11)`.

Therefore the favorable local classes `q|h`, which replace a `q-2` factor by `q-1`, cannot be treated as free average density gain. Their larger local survivor count is exactly balanced by the other shift classes when one averages through a full sieve period.

This is consistent with the earlier Fejér/gcd tariff findings `MC-464`--`MC-466`, but it is a different statement: `(11)` is an exact identity for the concrete rough×rough pair-sieve density, not an envelope estimate for the staged outer geometry.

## 5. Prior art and novelty boundary

The local factors in `(4)` are the elementary dimension-two shifted-sieve pattern already identified in `MC-471`; no novelty is claimed for them or for the associated singular-series language.

The complete rational-character phase belongs to classical finite-field character-sum theory. `MC-S55` anchors the more general Weil/Stepanov square-root bounds for mixed rational character sums used earlier in the line. Equation `(20)` is a simpler special complete correlation and is derived directly here rather than presented as a new estimate.

A targeted literature audit also found Jan-Christoph Schlage-Puchta, *Sifted character sums and free quotients of Bianchi groups*, Mathematical Proceedings of the Cambridge Philosophical Society 141 (2006), 205--207, DOI `10.1017/S0305004106009261`, which confirms that estimating character sums under sieve restrictions is established territory. Its sieve/character object is not the exact two-sided translated-ratio channel `(2)`.

The current audit also found Yixiu Xiao and Hongze Li, *Selberg sieve weights and sign changes of Kloosterman sums. I. Uniform asymptotics for shifted weights*, arXiv `2609.24248` (21 September 2026). Their Part I proves uniform asymptotics for correlations of shifted Selberg divisor weights and develops them for a later Kloosterman sign-change application. This is close modern prior art for retaining shifted sieve-weight structure, but it does not estimate the incomplete multiplicative-character pair sum `(12)`; no theorem transfer is asserted here.

Accordingly, **no novelty claim is made** for combining sieve and character-sum language. The Mathia-specific advance is the exact diagnosis of the current `MC-471` base channel: complete-period interaction factors, odd rough×rough shifts vanish, and the surviving load-bearing object is the incomplete discrepancy `(12)` plus the first-exit boundary channels from `MC-470`.

## Boundaries and falsification tests

- **Nonzero shift modulo `p` is essential.** If `h\equiv0 (mod p)`, then `(20)` is false: `K_h(n)=|chi(n)|^2` and the complete sum is `p-1`.
- **`W` must be coprime to `p`.** Equation `(8)` removes the conductor prime when necessary; identity `(9)` explains why this loses nothing in the character-weighted rough×rough sum.
- **The parity vanishing is rough×rough only.** The mixed `R_zE`, `ER_z`, and `EE` channels from `MC-471` need not vanish for odd `h`.
- **Complete-period factorization is not an incomplete estimate.** It cannot be promoted to a source-scale power saving without a new bound for `(12)`.
- **Local density is not phase cancellation.** The product `delta_W(h)` measures pair-sieve survival. Counting its logarithmic sparsity as the required conductor-power character saving would mix two different resources.
- **Shift averaging must preserve its actual kernel.** Equation `(11)` is uniform averaging modulo `W`; a Fejér-weighted shift sum requires a separate weighted analysis and cannot simply substitute `(11)`.
- **No Möbius or RH conclusion follows.** This finding narrows one internal pair-sieve source channel only.

## Consequence for the research line

The accepted staged-sieve clue should now treat the rough×rough base channel in two pieces.

Odd `h` can be removed exactly when `z>2`. For even `h`, the complete-period mean is already known and contains no special sieve/phase resonance. The next decisive object is the centered incomplete discrepancy `(12)` with `W=W_z`, or an equivalent representation that genuinely exposes new bilinear/dispersion structure while preserving the two-sided sieve condition.

A useful positive result must prove a strict conductor-power estimate for that incomplete discrepancy after the existing source-length, Fejér, endpoint, normalization and depth costs are charged. A useful negative result may show that available incomplete trace-function/sieve machinery cannot beat the source tariff. Re-deriving the local singular-series factors or the complete CRT product no longer advances the branch.

The positive first-exit boundary terms and nonempty rough-block/cross-component channels remain separate live possibilities.