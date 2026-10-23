# WI-454 — coherent Hankel differences recover all Hardy energy with a sharp calibration condition

**Status:** EXACT-DERIVED + CLASSICAL-IDENTITY + OPERATOR-CLASS-BOUNDARY + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** WI-441 (positive pure-tone bank obstruction), WI-437 (one-defect Hardy channels), WI-435 (the missing independent source bound).

## Exact boundary left open by the positive-bank obstruction

WI-441 excludes finite-energy positive banks of pure-tone Hankel operators, including bounded mixing of their Hilbert-space outputs. It explicitly leaves cancellation before forming that energy outside its scope. This distinction is substantive: a fixed, countable bank of coherent differences has operator norm one and preserves every shallow packet, without selecting a frequency after seeing the packet. However, its total energy is **exactly the original Hardy energy**. It supplies no independent arithmetic upper bound.

Use the unitary Fourier transform
\(\widehat f(\xi)=(2\pi)^{-1/2}\int f(t)e^{-it\xi}\,dt\),
and let \(\mathcal H_\pm\) denote the positive/negative Fourier half-spaces in \(L^2(\mathbb R)\). Write
\[
M_{-\omega}f(t)=e^{-i\omega t}f(t),\qquad
H_\omega=P_-M_{-\omega}|_{\mathcal H_+},
\]
and let \(E_I\) be the Fourier projection onto an interval \(I\). Fix any \(\Omega>0\), independently of a hypothetical divisor, and set \(\omega_j=2^j\Omega\), \(j\ge0\). Define
\[
D_j:=H_{2\omega_j}-M_{-\omega_j}H_{\omega_j}.
\tag{1}
\]
The second modulation maps \(\mathcal H_-\) into itself. The exact identities are
\[
\boxed{D_j=M_{-2\omega_j}E_{(\omega_j,2\omega_j)}|_{\mathcal H_+}},
\tag{2}
\]
\[
\boxed{\|H_\Omega f\|_2^2+\sum_{j\ge0}\|D_jf\|_2^2=\|f\|_2^2
\quad(f\in\mathcal H_+).}
\tag{3}
\]
Thus \(\mathscr A f=(H_\Omega f,D_0f,D_1f,\ldots)\) is an isometry from \(\mathcal H_+\) into a countable Hilbert direct sum of copies of \(\mathcal H_-\). No depth-dependent coefficients or unbounded output operator occur in this statement.

To prove (2), frequency shifting gives
\[
H_\omega f=M_{-\omega}E_{(0,\omega)}f.
\]
The two terms in (1), after their frequencies are aligned, therefore subtract the nested projections \(E_{(0,2\omega_j)}-E_{(0,\omega_j)}\). For every finite \(N\), orthogonality yields
\[
\|H_\Omega f\|_2^2+\sum_{j=0}^N\|D_jf\|_2^2
=\int_0^{2^{N+1}\Omega}|\widehat f(\xi)|^2\,d\xi.
\tag{4}
\]
Monotone convergence proves (3). This is a convergent sum of nonnegative energies of individually defined differences, not subtraction of two infinite energies. Frequency endpoints have Lebesgue measure zero.

## Shallow packets and the order of limits

For the normalized WI-441 packet
\[
\widehat u_{r,\gamma}(\xi)=\sqrt{2r}\,e^{-r\xi}e^{-i\gamma\xi}
\quad(\xi>0),\qquad r>0,
\]
the individual responses and truncated total are
\[
\|D_ju_{r,\gamma}\|_2^2
=e^{-2r\omega_j}-e^{-4r\omega_j},\qquad
\|\mathscr A_Nu_{r,\gamma}\|^2
=1-e^{-2r2^{N+1}\Omega}.
\tag{5}
\]
The full response is exactly one, uniformly in both parameters. Every fixed finite truncation is nevertheless shallow-blind as \(r\downarrow0\). The two iterated limits are respectively one and zero; the surviving energy moves to frequencies of order \(1/r\). Finite output energy does not mean finite bandwidth or a finite number of measurements.

There is no contradiction with WI-438's fixed-symbol obstruction or WI-441. The raw unweighted sequence \((H_{2^j\Omega}f)_{j\ge0}\) has infinite squared norm for every nonzero \(f\), since its component norms tend to \(\|f\|_2\). Although adjacent subtraction with modulation is a bounded operation on an abstract square-summable sequence space, that raw sequence is **not in its domain**. Equation (3) instead defines and bounds the composite directly through (4). It cannot factor through any of WI-441's fixed finite-packet-energy banks followed by a bounded map: such a factorization would force its packet response to vanish.

## Calibration errors: an exact necessary and sufficient budget

The cancellation has a sharp stability requirement. For arbitrary fixed complex scalars \(\varepsilon_j\), replace (1) by
\[
D_j^{\varepsilon}
:=H_{2\omega_j}-(1+\varepsilon_j)M_{-\omega_j}H_{\omega_j}.
\]
After the common modulation this is
\[
M_{-2\omega_j}\big(E_{(\omega_j,2\omega_j)}
-\varepsilon_jE_{(0,\omega_j)}\big).
\]
The two intervals are disjoint. Consequently, allowing infinite values,
\[
\boxed{\|\mathscr A_\varepsilon f\|^2
=\|f\|_2^2+\sum_{j\ge0}|\varepsilon_j|^2
\int_0^{\omega_j}|\widehat f(\xi)|^2\,d\xi.}
\tag{6}
\]
Here the low channel remains \(H_\Omega\). For any nonzero \(f\), the integrals in (6) tend to \(\|f\|_2^2>0\). Hence
\[
\boxed{\text{finite response on one nonzero input}
\iff (\varepsilon_j)\in\ell^2
\iff \mathscr A_\varepsilon\text{ is bounded on }\mathcal H_+.}
\tag{7}
\]
Indeed the exact operator norm is
\[
\boxed{\|\mathscr A_\varepsilon\|^2=1+\sum_j|\varepsilon_j|^2.}
\tag{8}
\]
The upper bound follows from (6), and equality holds for any unit input supported in Fourier space inside \((0,\Omega)\). A uniform small error bound alone is insufficient: a nonzero constant error produces infinite energy on every nonzero input. In contrast, square-summable errors are allowed, and on the shallow packets
\[
\|\mathscr A_\varepsilon u_{r,\gamma}\|^2
=1+\sum_j|\varepsilon_j|^2(1-e^{-2r\omega_j})
\longrightarrow1
\tag{9}
\]
uniformly in \(\gamma\), by dominated convergence. This condition concerns scalar gain mismatch with exact modulation; it is not a theorem for arbitrary phase, frequency, or measurement errors.

## What the bank preserves, and what it cannot establish

For the WI-437 single Kunik block at depth \(d\), multiplicity \(m\), and probe \(a=\theta d\), \(0<\theta<1\), equation (3) gives
\[
\|\mathscr A G_+\|^2=\|G_+\|_2^2
=\frac{\pi m^2}{(1-\theta)d}.
\tag{10}
\]
It therefore preserves the entire one-defect quantum at fixed operator norm, while requiring arbitrarily high frequencies for arbitrarily shallow defects.

It also preserves the old mixed pairing exactly. With the inner product linear in its first entry, \(\overline{G_-}\in\mathcal H_+\), so polarization of (3) gives
\[
\langle\mathscr A G_+,\mathscr A\overline{G_-}\rangle
=\langle G_+,\overline{G_-}\rangle
=\int G_+(t)G_-(t)\,dt
=\frac{\pi m^2}{d}.
\tag{11}
\]
Thus this fixed bank changes the representation and the admissible cancellation class, but not the quantity that must be controlled. The same isometry holds for every Hardy input, including finite artificial Kunik blocks. It does not distinguish the zeta source from those matched controls, prove that the full zeta channel is globally square integrable, or infer vanishing of its energy. In particular it leaves WI-435's missing independent source bound intact. Access to the unknown interior Hardy field cannot be treated as an unconditional prime-side estimate merely because (3) has operator norm one.

## Prior art, mathematical delta, and audit boundary

Dyadic frequency differences and their square-function energy are classical Littlewood--Paley/Plancherel theory. Authoritative exposition includes Terence Tao, *Lecture Notes 5 for 247A* (UCLA, 2006), pp. 10--11, [author's notes](https://www.math.ucla.edu/~tao/247a.1.06f/notes5.pdf). Those notes use smooth frequency partitions; the sharp disjoint-interval identity needed here is proved directly in (2)--(4). No new decomposition theorem, general Hankel theorem, or literature priority is claimed. The Hankel realization uses precisely the single-tone identity already established in WI-438/WI-441, rather than a different Bessel-type Hankel transform.

The delta is a constructive resolution of WI-441's excluded cancellation case together with the exact calibration criterion (7): bounded **composite** energy and fixed coefficients can coexist with perfect shallow sensitivity when overlapping outputs are cancelled before their energy is summed. The obstruction to an RH application is then the source bound, rather than a necessary divergence of the composite norm. Conversely, cancelling only approximately with a nonsquare-summable gain error restores the divergent repeated-low-frequency cost.

The decisive checks are the aligned-shift identity (2), disjointness in (6), and the two orders of limits in (5). They are exact for all \(L^2\) Hardy inputs and require neither numerical evidence nor a conjecture on zeros. This does not reopen the positive-bank theorem, and it does not justify pursuing the isometry itself as a new zero-exclusion mechanism. A subsequent source-specific proposal must establish additional arithmetic control of these channels; the present universal energy identity supplies none.
