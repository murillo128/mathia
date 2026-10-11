# WI-441 — finite-cost Hankel frequency banks are shallow-blind even after bounded mixing

**Status:** EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + LITERATURE+DERIVED + NO-NOVELTY-CLAIM

**Parents:** WI-436, WI-437, WI-438. The result concerns the individual off-line Kunik/Hardy defect channel, not a density-one certificate.

## 1. Precise obstruction

Let \(\mathcal H_+=H^2_+(\mathbb R)\), \(\mathcal H_-=H^2_-(\mathbb R)\), and for every \(\omega>0\) let

\[
H_\omega=P_-M_{e^{-i\omega t}}|_{\mathcal H_+}.
\]

These are exactly the noncompact norm-one Hankel partial isometries used as the frequency-scale witness in WI-438. Let \(\mu\) be any positive Borel measure on \((0,\infty)\), selected independently of a hypothetical off-line zero, and define the quadratic response of the bank by

\[
\mathcal Q_\mu(u):=\int_0^\infty\|H_\omega u\|_2^2\,d\mu(\omega).
\tag{1}
\]

No finite-mass assumption is imposed on \(\mu\). For the normalized positive Hardy packet of a single Kunik defect,

\[
\widehat u_{r,\gamma}(\xi)=\sqrt{2r}\,e^{-r\xi}e^{-i\gamma\xi}
\quad(\xi>0),
\]

one has the exact, ordinate-independent identity

\[
\boxed{\mathcal Q_\mu(u_{r,\gamma})
=\int_0^\infty(1-e^{-2r\omega})\,d\mu(\omega)=:F_\mu(r).}
\tag{2}
\]

If the bank is finite on this packet at even one positive scale,

\[
F_\mu(r_0)<\infty\quad\text{for some }r_0>0,
\tag{3}
\]

then necessarily

\[
\boxed{\lim_{r\downarrow0}F_\mu(r)=0,}
\tag{4}
\]

**uniformly in the ordinate \(\gamma\)**. In particular, no such source-fixed, positive frequency bank can supply a normalized order-one shallow-defect quantum for every \(0<r<r_0\).

This remains true if the outputs of the whole bank are subsequently mixed by any bounded, possibly signed and non-diagonal operator. Write \(\mathcal K_\mu=\int^\oplus\mathcal H_-\,d\mu(\omega)\) and \(\mathscr H_\mu u=(H_\omega u)_\omega\), initially on vectors with finite (1). Then

\[
\|\mathscr H_\mu u_{r,\gamma}\|_{\mathcal K_\mu}^2=F_\mu(r).
\]

For any \(B:\mathcal K_\mu\to\mathcal K_\mu\) with a norm bound independent of \(r,\gamma\),

\[
\boxed{
|\langle \mathscr H_\mu u_{r,\gamma},
 B\mathscr H_\mu u_{r,\gamma}\rangle|
\le \|B\| F_\mu(r)\longrightarrow0.
}
\tag{5}
\]

For every family of dual output vectors \(v_{r,\gamma}\) with uniformly bounded norm, likewise

\[
|\langle \mathscr H_\mu u_{r,\gamma},v_{r,\gamma}\rangle|
\le \sqrt{F_\mu(r)}\,\|v_{r,\gamma}\|\longrightarrow0.
\tag{6}
\]

Thus bounded post-bank mixing does not rescue the frequency portfolio. Equations (5)–(6) are conditional on a fixed finite-energy bank and a bounded output operation; they do not cover a depth-dependent unbounded rescaling.

## 2. Exact spectral normal form

Use the same unitary Fourier/Plancherel convention as WI-438. Multiplication by \(e^{-i\omega t}\) shifts frequency down by \(\omega\), and projection to negative frequencies retains exactly \(0<\xi<\omega\). Hence for every \(u\in\mathcal H_+\),

\[
\|H_\omega u\|_2^2
=\int_0^\omega|\widehat u(\xi)|^2\,d\xi.
\tag{7}
\]

Tonelli's theorem, requiring no a priori finite mass of \(\mu\), yields

\[
\boxed{
\mathcal Q_\mu(u)=
\int_0^\infty W_\mu(\xi)|\widehat u(\xi)|^2\,d\xi,
\qquad
W_\mu(\xi)=\mu((\xi,\infty)).
}
\tag{8}
\]

Endpoint atoms are irrelevant to the \(d\xi\) integral. The entire positive frequency bank is therefore a **single nonincreasing low-pass Fourier multiplier** at the level of its quadratic response. It does not generate a new high-frequency positive carrier by taking infinitely many high-frequency Hankel shifts.

For \(\widehat u_{r,\gamma}\) the right side of (8) is

\[
2r\int_0^\infty e^{-2r\xi}W_\mu(\xi)\,d\xi,
\tag{9}
\]

and Tonelli recovers (2). Since \(1-e^{-2r_0\omega}\) is comparable to \(\min\{1,\omega\}\) for each fixed \(r_0>0\), condition (3) is equivalent to

\[
\boxed{\int_0^\infty\min\{1,\omega\}\,d\mu(\omega)<\infty.}
\tag{10}
\]

This is the familiar Lévy-measure condition in the Bernstein-function representation of the Laplace exponent \(F_\mu(r)\). It allows infinite total \(\mu\)-mass near \(\omega=0\); in particular, the theorem is stronger than a finite-total-weight argument.

For \(0<r\le r_0\), the pointwise inequality
\(0\le1-e^{-2r\omega}\le1-e^{-2r_0\omega}\)
provides an integrable dominating function by (3), while the integrand tends to zero at every fixed \(\omega\). Dominated convergence proves (4). This also verifies that the direct-integral output is a well-defined Hilbert vector on the normalized test packets even when the full bank is not a bounded operator on all of \(\mathcal H_+\). No global boundedness of \(\mathscr H_\mu\) is silently inferred from (3).

## 3. The unbounded-frequency escape and its exact price

The result is sharp against the apparent loophole in WI-438 that a family of symbols with frequencies diverging as \(1/r\) ceases to be equicontinuous.

Take a dyadic bank with \(\omega_j=2^j\) and \(w_j=2^{-j}\), \(j\ge1\). Then

\[
F(r)=\sum_{j\ge1}2^{-j}(1-e^{-2^{j+1}r})
=O(r\log(1/r))\longrightarrow0
\qquad(r\downarrow0).
\tag{11}
\]

Nevertheless for every fixed \(r>0\),

\[
\sup_{j\ge1}\|H_{2^j}u_{r,\gamma}\|_2^2=1.
\tag{12}
\]

Each individual Hankel operator is norm-one and noncompact. Choosing the best *unweighted* frequency after knowing \(r\) gives a perfect response, but the same collection has vanishing fixed finite-weight quadratic response. With unweighted counting measure \(\mu=\sum_{j\ge1}\delta_{2^j}\), equation (2) is infinite for every \(r>0\): the missing order-one shallow sensitivity has been purchased by an infinite packet-energy budget.

More generally, (3)–(4) show that **every** positive frequency measure with finite packet cost somewhere, not merely dyadic or summable discrete weights, is shallow-blind. No special shape of the distribution of \(\omega\) evades that theorem.

## 4. Kunik defect comparison and research consequence

For a single right-half off-critical zero \(\rho=\frac12+d+i\gamma\), take the interior probe \(a=\theta d\) with fixed \(0<\theta<1\). The normalized positive Hardy channel of WI-437/WI-438 is \(u_{r,\gamma}\) with \(r=(1-\theta)d\). The canonical mixed pairing of the same one-zero Kunik block has normalized value \(\sqrt{1-\theta^2}\), whereas (4)–(6) show that every fixed finite-packet-cost frequency bank, even after bounded post-bank cross-frequency mixing, has normalized response \(o(1)\).

Using the exact norms in WI-437, the corresponding mixed response with uniformly bounded dual output norm is

\[
o_\theta\!\left(\frac{m^2}{d}\right)
\]

versus the canonical \(\pi m^2/d\) boundary-defect energy. The suppression is ordinate-uniform in this pure-tone bank model.

The obstruction is not merely compactness or equicontinuity. Even an infinite bank of noncompact operators at unbounded frequencies becomes a low-pass quadratic multiplier, and the finite-cost condition forces it to lose the high-frequency packets representing arbitrarily shallow defects. Therefore the surviving program cannot consist only of adding more source-independent frequencies and then applying a bounded operator to their outputs.

## 5. Prior art, limitations, and falsification

The Hardy projection identity (7), Tonelli, dominated convergence, and the Lévy/Bernstein integral condition (10) are classical. WI-438 already establishes the single-tone formula \(1-e^{-2r\omega}\) and its noncompact-Hankel origin. Schilling–Song–Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed. (2012), DOI 10.1515/9783110269338, is standard prior art for the Laplace representation and integrability condition; no new Bernstein-function theorem or novelty priority is claimed here.

The actual delta relative to WI-438 is the exact arbitrary-measure spectral normal form (8), the finite-cost one-scale-to-zero theorem (3)–(4), and its stability under every bounded **non-diagonal** post-bank mixing (5)–(6). WI-426/WI-427 concern positive vertical-line portfolios of Kunik logarithmic-derivative norms, not frequency-shift Hankel banks; WI-317 concerns finite scalar localization portfolios. None of those results is used to infer an unsupported claim about all operator classes.

Important boundaries:

- Arbitrary bounded-symbol Hankel operators not representable as the indicated fixed positive bank of pure shifts are outside this no-go.
- Signed/source-correlated **pre-bank** mechanisms, scale-dependent frequency selection, and mixing operators whose norm diverges with the target depth are not excluded; they require their own source-independent budget and normalization.
- A bank selected after inspecting the hypothetical zero ordinate or depth is oracle information, not an arithmetic detector. The theorem does not prove that zeta's independent source selects such a bank.
- Finite response for one isolated packet is not a proven source bound for the full zeta divisor; this is a matched one-defect falsifier of a proposed auxiliary architecture, not a statement that off-line zeta zeros exist or do not exist.
- The normal form is positive-frequency-bank-specific. No inference is made that every noncompact or nonlocal cross-channel operator is a low-pass multiplier.

A decisive falsifier of the theorem would be a positive measure \(\mu\) with \(F_\mu(r_0)<\infty\) but \(\limsup_{r\downarrow0}F_\mu(r)>0\); the dominated-convergence proof excludes it. To escape the mechanism scientifically, supply a source-valid mixed observable which cannot factor through (8) with a bounded post-bank operator, and show on the exact one-defect Kunik packet that its normalized response remains order one **with a budget fixed independently of the unknown divisor**. Merely taking more tones, claiming global noncompactness, or optimizing a free unweighted supremum does not pass that test.

This closes the fixed finite-cost pure-tone Hankel-bank extension of WI-438; it does not close the source-structured mixed-frequency/individual-defect route or prove RH.
